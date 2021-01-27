from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode


from database import conceptes_list

def busca(update: Update, context: CallbackContext) -> None:

    concepte = update.message.text.split("/busca ")[1]
    respostes = [item for item in conceptes_list if concepte in item["concepte"].casefold()]

    quantitat_r = len(respostes)
    update.message.reply_text("He trobat "+str(quantitat_r)+" respostes")

    for resposta in respostes:
        update.message.reply_text(
            text="segons m'ha dit<b> " + resposta["usuari"] + "</b>:" + "\n" + resposta["concepte"]+" (record: "+resposta["memoria"]+") ",
            parse_mode=ParseMode.HTML)

