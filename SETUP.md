# RTB Social Media UTM Dashboard — Setup

## Files
- `RTB Social Media UTM Dashboard.html` — the dashboard (self-contained).
- `data/utm-log.json` — the shared log everyone reads/writes. Starts as `[]`.

## Deploy to GitHub Pages
Put both items in the repo (`quinn-weathers/rtb-marketing-projects`), keeping the
`data/` folder next to the HTML. Suggested repo path: `Social Media UTM/`.

Live URL will be:
`https://quinn-weathers.github.io/rtb-marketing-projects/Social%20Media%20UTM/RTB%20Social%20Media%20UTM%20Dashboard.html`
(A folder with no spaces, e.g. `social-media-utm/`, makes for a cleaner link.)

## One-time: connect the shared log (Social Media Director)
The site is static, so the **Generate** button commits new links to `utm-log.json`
using a GitHub token entered once and stored **only in his browser** (never in the repo).

1. GitHub → Settings → Developer settings → **Fine-grained tokens** → Generate new token.
2. Repository access: **Only select repositories** → `rtb-marketing-projects`.
3. Permissions → Repository permissions → **Contents: Read and write**.
4. Copy the token. In the dashboard, click **Connect GitHub** (sidebar), confirm
   owner / repo / branch / data path, paste the token, **Save & Test**.

After that, every **Generate** builds the link, copies it, and writes it to the shared
log so all visitors see it. Visitors without a token can still view, search, and export
the log (read-only).

## Tabs
- **UTM Builder** — enter link + answer the questions; Generate normalizes everything
  to lowercase-hyphenated, builds the tagged URL, copies it, and logs it.
- **UTM Log** — full team log; search, sort, filter by source, **Download Excel**.
- **Performance** — drop a GA4 CSV export (Acquisition → Traffic acquisition → Download CSV)
  to chart sessions/conversions by campaign/source; plus log-based charts that work
  immediately.

## Data path config
If you change where the data file lives in the repo, update **Data file path** in the
Connect dialog to match (path relative to repo root).
