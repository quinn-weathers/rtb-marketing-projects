# RTB Marketing Projects Dashboard

Daily-updating team dashboard for Right To Bear, showing task assignments and workload across the marketing team.

## 🚀 Quick Setup (GitHub Pages)

### 1. Create Repository
1. Create a new **public** repository on GitHub
2. Name it `rtb-marketing-projects`
3. Upload all files from this folder

### 2. Enable GitHub Pages
1. Go to repository Settings → Pages
2. Under "Source", select `main` branch
3. Click Save
4. Your site will be live at: `https://[your-username].github.io/rtb-marketing-projects/`

### 3. Add Monday.com API Token
1. In your repository, go to Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `MONDAY_API_TOKEN`
4. Value: Paste your Monday.com API token
5. Click "Add secret"

### 4. Update Board IDs (if needed)
Edit `fetch_data.py` and update the `BOARD_IDS` array with your actual board IDs:

```python
BOARD_IDS = [
    "9533201616",    # Marketing Requests
    "18004001679",   # Blog Content Creative Requests
    "17945827124"    # Social Media Creative Requests
]
```

### 5. Test the Workflow
1. Go to Actions tab in your repository
2. Click "Update Dashboard Data" workflow
3. Click "Run workflow" → "Run workflow"
4. Wait ~1 minute, then refresh your GitHub Pages site

## ⏰ Automatic Updates

The dashboard automatically updates **daily at 6 AM UTC** (1 AM EST / 10 PM PST).

You can also trigger manual updates:
1. Go to Actions tab
2. Select "Update Dashboard Data"
3. Click "Run workflow"

## 🔗 Sharing Personal Links

1. Open the dashboard at your GitHub Pages URL
2. Scroll to bottom → "Admin Tools" section
3. Click any team member's name to copy their personal link
4. Share that link with them

When they open it, they'll see ONLY their tasks with no ability to switch views.

## 📁 Files Explanation

- `index.html` - The dashboard (loads data from data.json)
- `data.json` - Task and team data (auto-updated daily)
- `fetch_data.py` - Python script that pulls from Monday.com
- `.github/workflows/update-data.yml` - GitHub Action for daily updates

## 🔧 Troubleshooting

**Dashboard shows error**: Check that `data.json` exists in the repository

**Data not updating**: 
1. Check Actions tab for errors
2. Verify your `MONDAY_API_TOKEN` secret is set correctly
3. Make sure the workflow has permission to commit (Settings → Actions → General → Workflow permissions → "Read and write")

**Links don't work**: Make sure you're using the full GitHub Pages URL, not a local file path

## 📊 Data Source

Pulls from 3 Monday.com boards:
- Marketing Requests
- Blog Content Creative Requests  
- Social Media Creative Requests

Only shows incomplete items (status ≠ Done/Complete).
