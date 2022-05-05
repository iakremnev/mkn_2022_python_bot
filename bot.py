from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


TOKEN = ...


def hello(update: Update, context: CallbackContext) -> None:
    """Greet user saying /hello"""
    update.message.reply_text(f"Hello {update.effective_user.first_name}")


def help(update: Update, context: CallbackContext) -> None:
    """Help on commands"""
    commands_with_descriptions = []
    for handler_list in updater.dispatcher.handlers.values():
        for handler in handler_list:
            command_repr = "\n".join(["/" + comm for comm in handler.command])
            docstring = handler.callback.__doc__
            commands_with_descriptions.append(command_repr + "\n" + docstring)
    update.message.reply_text("\n-----\n".join(commands_with_descriptions))


updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
updater.idle()
