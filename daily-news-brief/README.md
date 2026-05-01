# RTB · 2A Daily Intel — Marketing Brief

**Live URL:** https://quinn-weathers.github.io/rtb-marketing-projects/daily-news-brief/

## What this is

The daily 2A / firearm-industry / political news brief for the Right To Bear marketing team. Generated every weekday at 6:00 AM ET by an automated pipeline running on Quinn's workstation.

## How it gets here

1. The scheduled task `bear-2a-daily-brief` (in Cowork) runs at 6 AM ET on weekdays.
2. It scans Congress.gov, SCOTUSblog, the Federal Register, LegiScan, USCCA blog, AP gun politics, Politico, Pew, and a dozen other sources.
3. It diffs against a state file (`News\_state\tracking.json`) to identify NEW / MOVED / WATCH items.
4. It computes a heat score (0-100) for each item from Google Trends, X, Reddit, and news pickup.
5. It writes the brief to `index.html` (rolling) and `archive/RTB_2A_Brief_YYYY-MM-DD.html` (dated archive).
6. It commits and pushes to this folder of the repo.
7. GitHub Pages auto-deploys within ~60 seconds.
8. A summary card posts to the marketing Teams channel via the configured webhook.

## Folder structure

```
daily-news-brief/
├── index.html                          # Latest brief (overwritten daily)
├── archive/
│   ├── RTB_2A_Brief_2026-04-30.html    # Daily archives
│   └── ...
└── README.md                           # This file
```

## Re-deployment / troubleshooting

If the daily push stops working:

1. Check Cowork → Scheduled → `bear-2a-daily-brief` for the last run status.
2. Make sure GitHub Desktop is signed in on the host workstation.
3. Confirm `News\_state\github_repo_path.txt` still points at the local clone path.
4. Confirm GitHub Pages is enabled on this repo (Settings → Pages → main branch / root).

## Editorial guardrails

Brief copy is factual, evenhanded, source-linked, and empowerment-led — not fear-only. This follows the RTB Brand Guide 11-20-2025.
