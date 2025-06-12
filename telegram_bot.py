import os
import django
from telegram.ext import Updater, CommandHandler
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from core.models import TelegramUser

def start(update, context):
    print("✅ Received /start command")  # Debug
    user = update.effective_user
    username = user.username
    print(f"Username: {username}")  # Debug

    if not username:
        update.message.reply_text("⚠️ Your Telegram username is missing. Please set it in your Telegram settings.")
        return

    if TelegramUser.objects.filter(username=username).exists():
        update.message.reply_text(f"✅ You’re already registered, {username}.")
    else:
        TelegramUser.objects.create(username=username)
        update.message.reply_text(f"👋 Hello {username}! You’ve been registered successfully.")

def main():
    updater = Updater(config("TELEGRAM_BOT_TOKEN"), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    print("✅ Telegram bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()