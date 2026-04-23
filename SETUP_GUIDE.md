# Complete GitHub Pages Setup Guide

## Part 1: Get Your Monday.com API Token

1. Log into Monday.com
2. Click your profile picture (bottom left)
3. Select **Admin**
4. Go to **API** section (left sidebar)
5. Under "API v2 Token":
   - If you have an existing token, copy it
   - If not, click "Generate" and copy the new token
6. **Save this token somewhere safe** - you'll need it in Part 3

---

## Part 2: Create GitHub Repository

1. Go to [github.com](https://github.com) and sign in
2. Click the **+** icon (top right) → **New repository**
3. Fill out the form:
   - **Repository name**: `rtb-marketing-projects`
   - **Description**: "Team dashboard for RTB marketing tasks"
   - **Public** ✓ (required for free GitHub Pages)
   - **Initialize this repository with**: Leave unchecked
4. Click **Create repository**

---

## Part 3: Upload Files

### Option A: Upload via Web Interface (Easier)

1. In your new repository, click **uploading an existing file**
2. Drag and drop ALL files from the folder I gave you:
   - `index.html`
   - `data.json`
   - `fetch_data.py`
   - `README.md`
   - `.gitignore`
   - `.github/` folder (entire folder with workflows inside)
3. Scroll down and click **Commit changes**

### Option B: Upload via Git Command Line

```bash
cd path/to/github-setup
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/rtb-marketing-projects.git
git push -u origin main
```

---

## Part 4: Enable GitHub Pages

1. In your repository, click **Settings** (top menu)
2. In left sidebar, click **Pages**
3. Under "Source":
   - Branch: **main**
   - Folder: **/ (root)**
4. Click **Save**
5. Wait 1-2 minutes, then refresh the page
6. You'll see: "Your site is live at `https://YOUR-USERNAME.github.io/rtb-marketing-projects/`"
7. **Copy this URL** - this is your dashboard's permanent link!

---

## Part 5: Add Monday.com API Token as Secret

1. Still in Settings, scroll down left sidebar to **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Fill in:
   - **Name**: `MONDAY_API_TOKEN` (must be exactly this)
   - **Value**: Paste the token you copied in Part 1
4. Click **Add secret**

---

## Part 6: Configure Workflow Permissions

1. Still in Settings, click **Actions** → **General** (left sidebar)
2. Scroll to "Workflow permissions"
3. Select **Read and write permissions**
4. Check ✓ "Allow GitHub Actions to create and approve pull requests"
5. Click **Save**

---

## Part 7: Update Board IDs (Important!)

The Python script needs your actual Monday.com board IDs. Here's how to get them:

1. Open each board in Monday.com
2. Look at the URL: `https://right-to-bear-association.monday.com/boards/9533201616`
3. The number at the end (`9533201616`) is the board ID
4. In your GitHub repository, click `fetch_data.py`
5. Click the **pencil icon** (Edit)
6. Find this section:

```python
BOARD_IDS = [
    "9533201616",    # Marketing Requests
    "18004001679",   # Blog Content Creative Requests
    "17945827124"    # Social Media Creative Requests
]
```

7. Replace with YOUR board IDs
8. Scroll down, click **Commit changes**

---

## Part 8: Run First Update (Test)

1. Go to **Actions** tab (top menu)
2. You'll see "Update Dashboard Data" workflow
3. Click it
4. Click **Run workflow** (right side)
5. Click the green **Run workflow** button
6. Wait 30-60 seconds
7. Click on the workflow run to see progress
8. When it turns green ✓, data has been fetched!

---

## Part 9: Check Your Dashboard

1. Go to your GitHub Pages URL: `https://YOUR-USERNAME.github.io/rtb-marketing-projects/`
2. You should see the full dashboard with fresh Monday.com data!
3. If you see an error, go back to Actions tab and check for error messages

---

## Part 10: Share Personal Links

1. Open the dashboard
2. Scroll all the way to the bottom
3. You'll see "Admin Tools — Generate Personal Links"
4. Click any team member's name
5. Their unique link is copied to clipboard
6. Paste into Slack/email to send to them

Example link: `https://YOUR-USERNAME.github.io/rtb-marketing-projects/?member=97224167&lock=true`

When they open it:
- ✓ Only see their own tasks
- ✓ No dropdown to switch people
- ✓ No admin tools section

---

## Automatic Daily Updates

✅ The dashboard will automatically update every day at 6 AM UTC (1 AM EST)

You can also trigger updates manually anytime:
1. Go to Actions tab
2. Click "Update Dashboard Data"
3. Run workflow

---

## Troubleshooting

### "Error Loading Dashboard"
- Check that `data.json` exists in your repository
- Try running the workflow again (Actions → Run workflow)

### Data Not Updating
- Go to Actions tab, click the failed run to see error
- Most common: API token is wrong or missing
- Fix: Settings → Secrets → Edit `MONDAY_API_TOKEN`

### Personal Links Give "404 Not Found"
- Make sure you're using the FULL GitHub Pages URL
- NOT: `file:///C:/Users/...`
- YES: `https://username.github.io/rtb-marketing-projects/...`

### Workflow Fails with "Permission denied"
- Settings → Actions → General
- Workflow permissions → "Read and write permissions"
- Save

---

## You're Done! 🎉

Your dashboard is now:
- ✅ Live on the web
- ✅ Auto-updating daily
- ✅ Shareable with personal links
- ✅ Pulling fresh data from Monday.com

Dashboard URL: `https://YOUR-USERNAME.github.io/rtb-marketing-projects/`
