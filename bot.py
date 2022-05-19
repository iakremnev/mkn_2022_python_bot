from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, filters
from telegram.ext import MessageHandler
import text_effects

import random

with open("stopwords-ru.txt") as f:
    STOP_WORDS = f.read().split()
STOP_WORDS = set(STOP_WORDS)

TOKEN = ...


def hello(update: Update, context: CallbackContext) -> None:
    """Greet user saying /hello"""
    update.message.reply_text(f"Hello {update.effective_user.first_name}")


def help(update: Update, context: CallbackContext) -> None:
    """Description of all commands"""
    commands_with_descriptions = []
    for handler_list in updater.dispatcher.handlers.values():
        for handler in handler_list:
            command_repr = "\n".join(["/" + comm for comm in handler.command])
            docstring = handler.callback.__doc__
            commands_with_descriptions.append(command_repr + "\n" + text_effects.italics(docstring))
    delimiter = "\n" + text_effects.bold("=" * 32) + "\n"
    update.message.reply_markdown_v2(delimiter.join(commands_with_descriptions))


def what_is(update: Update, context: CallbackContext) -> None:
    text: str = update.message.text
    word_to_choose_from = set(text.split()) - STOP_WORDS
    if len(word_to_choose_from) == 0:
        answer = "В чем смысл жизни?"
    else:
        word = random.choice(list(word_to_choose_from))
        answer = f"Что такое {word}?"
    update.message.reply_text(answer)


updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(
    MessageHandler(
        filters=(filters.Filters.text & ~filters.Filters.command),
        callback=what_is
    )
)

updater.start_polling()
updater.idle()
