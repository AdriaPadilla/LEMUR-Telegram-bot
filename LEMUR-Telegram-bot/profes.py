from telegram import ParseMode
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def profes(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='Hola! El meu nom és L.E.M.U.R, i sóc un bot en desenvolupament creat amb Python. Els meus creadors estan treballant per afegir-me funcionalitats. De moment, puc <b>aprendre</b> i <b>buscar</b> conceptes... però no gaire cosa més. :(' +"\n"+"\n" +
             "Els meus creadors son:" +"\n" +
             '<b><a href="www.twitter.com/xribes/">@XavierRibes</a></b>' +"\n"+
             '<b><a href="www.twitter.com/adriapadilla/">@AdriaPadilla</a></b>',
        parse_mode=ParseMode.HTML)