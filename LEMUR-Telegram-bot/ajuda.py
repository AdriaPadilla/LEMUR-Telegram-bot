from telegram import ParseMode
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text="Benvingut a <b>L.E.M.U.R.</b>, Què vols fer?:"+"\n"+"\n"+
            "<b>/apren</b> per ensenyar-me un concepte nou."+"\n"+"\n"+
            "<b>/busca</b> per obtenir informació sobre un concepte."+"\n"+"\n"+
            "<b>/info</b> per saber qui m'ha creat.",
        parse_mode=ParseMode.HTML)