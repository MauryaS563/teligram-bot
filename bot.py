from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "YAHAN_APNA_BOT_TOKEN_DALIYE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 Welcome!\n\nBot successfully working."
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()
BOT_TOKEN = "8906680825:AAFS5KfbW41HrRihhUTADCxpH9W907SiU00"