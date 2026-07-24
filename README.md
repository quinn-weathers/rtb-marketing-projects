# RTB Marketing Projects

Internal tools and dashboards for the Right To Bear marketing team, hosted as a static site on GitHub Pages.

**Live:** https://quinn-weathers.github.io/rtb-marketing-projects/

The home page (`index.html`) is a simple hub that links out to each tool below.

## Pages

| Page | URL | What it is |
|------|-----|------------|
| Spiderweb | `/spiderweb/` | Marketing org command center — pipelines in play, departments and leads, flagged/overdue items, and the weekly view. |
| Daily brief | `/daily-news-brief/` | 2A and firearm-industry daily news brief. Auto-generated each weekday around 6:00 AM ET. |
| Weekly brief | `/weekly-news-brief/` | Friday 2A weekly recap and forward-look. |
| UTM builder | `/social-media-utm.html` | Builds UTM-tagged campaign links for the team and logs them to `utm-log.json`. |
| Share on social | `/share-on-social.html` | Ready-to-post social copy feed. |

> `RTB Social Media UTM Dashboard.html` is an older duplicate of the UTM builder, kept in case its link was shared previously. `social-media-utm.html` is the current one.

## Automation

`.github/workflows/post-rtb-brief-to-teams.yml` relays the daily brief to the marketing Teams channel. It fires when the brief generator pushes `daily-news-brief/_teams_card.json`, then POSTs that adaptive card to a Teams webhook. It needs a `TEAMS_WEBHOOK_URL` repository secret (Settings → Secrets and variables → Actions) and can be re-fired manually from the Actions tab.

The daily and weekly briefs themselves are generated outside this repo by scheduled Cowork tasks that commit and push their results here. GitHub Pages redeploys within about a minute of any push.

## Editing

Everything here is static HTML. Edit a file, commit to `main`, and GitHub Pages redeploys automatically. To add a new tool, drop its page in the repo and add a matching card to `index.html`.

## Legacy (no longer active)

This repo originally served a Monday.com-powered task dashboard on the home page, refreshed daily by an `update-data.yml` workflow. That workflow was removed on 2026-07-24 after its Monday.com API token stopped authenticating (HTTP 401 Unauthorized), and the home page was replaced with the hub above. Two leftover files from that setup — `fetch_data.py` and `data.json` — are no longer used and can be deleted whenever you like.
