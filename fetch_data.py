#!/usr/bin/env python3
"""
Fetch team and task data from Monday.com and save to data.json
"""
import os
import json
import requests
from datetime import datetime

# Monday.com API configuration
API_URL = "https://api.monday.com/v2"
API_TOKEN = os.environ.get("MONDAY_API_TOKEN")

# Board IDs - UPDATE THESE WITH YOUR ACTUAL BOARD IDs
BOARD_IDS = [
    "9533201616",    # Marketing Requests
    "18004001679",   # Blog Content Creative Requests
    "9668868754"    # Social Media Creative Requests
]

def query_monday(query):
    """Execute a GraphQL query against Monday.com API"""
    headers = {
        "Authorization": API_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.post(API_URL, json={"query": query}, headers=headers)
    response.raise_for_status()
    return response.json()

def get_users():
    """Fetch all users from Monday.com workspace"""
    query = """
    {
      users {
        id
        name
        title
        photo_thumb_small
      }
    }
    """
    result = query_monday(query)
    users = result["data"]["users"]
    
    # Transform to TEAM format
    team = []
    for user in users:
        team.append({
            "id": int(user["id"]),
            "name": user["name"],
            "role": user.get("title") or "Team Member",
            "photo": user.get("photo_thumb_small") or ""
        })
    
    return team

def get_board_tasks(board_id):
    """Fetch incomplete tasks from a specific board"""
    query = f"""
    {{
      boards(ids: {board_id}) {{
        name
        items_page(limit: 200, query_params: {{rules: [{{column_id: "status", compare_value: [5], operator: not_any_of}}]}}) {{
          items {{
            id
            name
            column_values {{
              id
              text
              value
            }}
          }}
        }}
      }}
    }}
    """
    result = query_monday(query)
    
    if not result["data"]["boards"]:
        return []
    
    board = result["data"]["boards"][0]
    board_name = board["name"]
    items = board["items_page"]["items"]
    
    tasks = []
    for item in items:
        # Parse column values
        columns = {col["id"]: col for col in item["column_values"]}
        
        # Extract assignees
        assignees = []
        if "people" in columns and columns["people"]["value"]:
            people_data = json.loads(columns["people"]["value"])
            assignees = [p["name"] for p in people_data.get("personsAndTeams", [])]
        
        # Extract approvers
        approvers = []
        if "people1" in columns and columns["people1"]["value"]:
            approver_data = json.loads(columns["people1"]["value"])
            approvers = [p["name"] for p in approver_data.get("personsAndTeams", [])]
        
        # Extract date
        date = None
        if "date4" in columns and columns["date4"]["text"]:
            date = columns["date4"]["text"]
        
        # Extract status
        status = columns.get("status", {}).get("text", "DISCOVERY")
        
        # Extract priority
        priority = columns.get("priority", {}).get("text", "")
        
        # Extract summary
        summary = columns.get("text", {}).get("text", "")
        
        tasks.append({
            "board": board_name,
            "short": board_name[:3].upper(),
            "id": item["id"],
            "name": item["name"],
            "url": f"https://right-to-bear-association.monday.com/boards/{board_id}/pulses/{item['id']}",
            "assignees": assignees,
            "approvers": approvers,
            "date": date,
            "status": status,
            "priority": priority,
            "summary": summary
        })
    
    return tasks

def main():
    """Main function to fetch data and save to JSON"""
    print("Fetching data from Monday.com...")
    
    # Fetch team
    print("→ Getting users...")
    team = get_users()
    print(f"  Found {len(team)} team members")
    
    # Fetch tasks from all boards
    all_tasks = []
    for board_id in BOARD_IDS:
        print(f"→ Getting tasks from board {board_id}...")
        tasks = get_board_tasks(board_id)
        all_tasks.extend(tasks)
        print(f"  Found {len(tasks)} incomplete tasks")
    
    # Create data structure
    data = {
        "team": team,
        "tasks": all_tasks,
        "last_updated": datetime.utcnow().isoformat() + "Z"
    }
    
    # Save to JSON
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"\n✓ Saved {len(team)} team members and {len(all_tasks)} tasks to data.json")
    print(f"✓ Last updated: {data['last_updated']}")

if __name__ == "__main__":
    main()
