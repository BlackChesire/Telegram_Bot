import Constans as keys
from telegram.ext import *
import Responses as R


def start_command(update, context):
    update.message.reply_text('היי אני הבוט של תל חי ואני כאן כדי לעזור')


def help_command(update, context):
    update.message.reply_text('אפשר לקבל פרטים כגון: .............')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused an error {context.error}")


def update_msg():
    pass


def main():
    cmd = input("choose a command for the bot (start,edit,exit): ")
    if cmd.lower() == "start" or cmd.lower().startswith("s"):
        updater = Updater(keys.API_KEY, use_context=True)
        dp = updater.dispatcher
        # dp.add_handler(CommandHandler("start", start_command))
        dp.add_handler(CommandHandler("help", help_command))
        dp.add_handler(MessageHandler(Filters.text, handle_message))
        dp.add_error_handler(error)
        updater.start_polling()
        updater.idle()
    if cmd.lower() == "edit" or cmd.lower().startswith("e"):
        pass
    else:
        exit()


main()
