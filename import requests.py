import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace with your own API token
API_TOKEN = "7278161266:AAEW3XEIlQhM_KurQJT54pOaujV_pN7j7RE"

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I am your bot. Send /help to see the list of available commands.")

async def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/info - Get bot information\n"
        "/temperature - Get the current temperature in Bucharest"
    )
    await update.message.reply_text(help_text)

async def info(update: Update, context: CallbackContext) -> None:
    bot_info = (
        f"Bot Name: {context.bot.name}\n"
        f"Username: {context.bot.username}\n"
        f"ID: {context.bot.id}"
    )
    await update.message.reply_text(bot_info)

async def get_temperature(update: Update, context: CallbackContext) -> None:
    city = "Bucharest"
    url = f"http://wttr.in/{city.replace(' ', '+')}?format=%t"

    response = requests.get(url)
    if response.status_code == 200:
        temperature = response.text.strip()
        await update.message.reply_text(f"The current temperature in {city} is {temperature}.")
    else:
        await update.message.reply_text("Sorry, unable to fetch the temperature at the moment.")

def main() -> None:
    application = Application.builder().token(API_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("temperature", get_temperature))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
