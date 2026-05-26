
# Telegram Prayer Tracker Bot

This bot lets you:
- Report your daily prayers through Telegram
- Automatically save the records into Google Sheets
- Keep a prayer recap history

---

# FEATURES

Supported prayers:
- subuh
- dzuhur
- ashar
- maghrib
- isya

Example messages:
- subuh
- dzuhur jamaah
- maghrib telat
- isya masjid

---

# INSTALLATION

## 1. Install Python packages

Open terminal:

pip install python-telegram-bot gspread oauth2client

---

## 2. Create Telegram Bot

1. Open Telegram
2. Search:
   @BotFather
3. Send:
/newbot
4. Follow instructions
5. Copy your bot token

Replace this line inside bot.py:

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

---

# GOOGLE SHEETS SETUP

## 1. Create Google Cloud Project

Go to:
https://console.cloud.google.com/

Create a project.

---

## 2. Enable APIs

Enable:
- Google Sheets API
- Google Drive API

---

## 3. Create Service Account

Create Service Account.

Generate JSON credentials.

Download the JSON file.

Rename it to:

credentials.json

Place it beside bot.py

---

## 4. Share Your Google Sheet

Create a Google Sheet named:

Prayer Tracker

Share the sheet with your service account email.

Example:
mybot@project-id.iam.gserviceaccount.com

Give Editor access.

---

# GOOGLE SHEET FORMAT

Headers recommended:

| Date | Time | User | Prayer | Notes |

The bot will append rows automatically.

---

# RUN BOT

python bot.py

---

# OPTIONAL IMPROVEMENTS

You can later add:
- Daily recap
- Missed prayer statistics
- Monthly charts
- Reminder notifications
- Tahajjud tracking
- Auto streak counter
- Web dashboard
