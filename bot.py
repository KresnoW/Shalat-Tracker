
import logging
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# =========================
# CONFIG
# =========================
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
GOOGLE_SHEET_NAME = "Prayer Tracker"

# =========================
# GOOGLE SHEETS SETUP
# =========================
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",
    scope
)

client = gspread.authorize(credentials)
sheet = client.open(GOOGLE_SHEET_NAME).sheet1

# =========================
# LOGGING
# =========================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# =========================
# START COMMAND
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Prayer Tracker Bot Ready.\n\n"
        "Send prayer names like:\n"
        "- subuh\n"
        "- dzuhur\n"
        "- ashar\n"
        "- maghrib\n"
        "- isya\n\n"
        "You can also send:\n"
        "subuh jamaah\n"
        "isya telat"
    )

# =========================
# SAVE TO GOOGLE SHEET
# =========================
async def save_prayer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text.strip()

    prayer_list = ["subuh", "dzuhur", "ashar", "maghrib", "isya"]

    detected = None
    for prayer in prayer_list:
        if prayer in text.lower():
            detected = prayer
            break

    if not detected:
        await update.message.reply_text(
            "Prayer not recognized. Example:\nsubuh\nmaghrib jamaah"
        )
        return

    now = datetime.now()

    row = [
        now.strftime("%Y-%m-%d"),
        now.strftime("%H:%M:%S"),
        user.full_name,
        detected,
        text
    ]

    sheet.append_row(row)

    await update.message.reply_text(
        f"Recorded: {detected.capitalize()} ✅"
    )

# =========================
# MAIN
# =========================
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_prayer))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
