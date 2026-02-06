import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv8447501351:AAFNL7ggNuzqLWbe02TcQFKFN0tGFz9_uX8

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👑 IMPERIAL\n\n"
        "Добро пожаловать в IMPERIAL — премиальный проект Telegram.\n\n"
        "Один шанс.\n"
        "Чёткие правила.\n"
        "Эксклюзивные возможности."
    )

    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
