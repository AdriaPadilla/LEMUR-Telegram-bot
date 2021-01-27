#!/usr/bin/env python
# pylint: disable=W0613, C0116
# type: ignore[union-attr]

# MODULS TELEGRAM

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
from telegram import Update


# MODULS PROPIS
import aprenentatge as aprenentatge
import buscador as buscador
import ajuda as ajuda
import profes as prof
import oblida as oblida

# FER EL LOGIN
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# FUNCIO PER A RESPOSTES RANDOM
def random(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("L'Adrià encara no m'ha programat per mantenir converses i només puc rebre instruccions, utilitza /ajuda per veure tot el que puc fer ;)")

def main():
    updater = Updater("", use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("apren", aprenentatge.apren))
    dispatcher.add_handler(CommandHandler("busca", buscador.busca))
    dispatcher.add_handler(CommandHandler("ajuda", ajuda.help_command))
    dispatcher.add_handler(CommandHandler("info", prof.profes))
    dispatcher.add_handler(CommandHandler("oblida", oblida.borrar))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, random))

    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()