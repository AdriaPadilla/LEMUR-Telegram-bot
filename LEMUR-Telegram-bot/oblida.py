from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode


from database import conceptes_list

def borrar(update: Update, context: CallbackContext) -> None:

    memoria = update.message.text.split("/oblida ")[1]
    respostes = [item for item in conceptes_list if memoria in item["memoria"]]
    for resposta in respostes:
        update.message.reply_text(
            text="He oblidat: "+ resposta["concepte"],
            parse_mode=ParseMode.HTML)
        conceptes_list.remove(resposta)


