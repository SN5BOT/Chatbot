import responses as res
from telegram.ext import *
import configparser as cfg
print("Bot started")

def start_command(update,context):
    update.message.reply_text('Type something to get started!')

def help_command(update, context):
    update.message.reply_text('More help? Find on Google')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = res.sample_responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f'Update {update} caused error {context.error}')

def read_token_from_config_file(config):
    parser = cfg.ConfigParser()
    parser.read(config)
    return parser.get('creds', 'token')

def main():
    updater = Updater(str(read_token_from_config_file("config.cfg")), use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()