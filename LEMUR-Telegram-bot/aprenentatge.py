from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from datetime import datetime

now = datetime.now()
from database import conceptes_list
from tweet_module import tweet

# FUNCIO APRENENTATGE
def apren(update: Update, context: CallbackContext) -> None:

    # Guardar la informació que ha enviat l'usuari

    concepte = update.message.text.split("/apren ")[1]

    try:
        nom_usuari = str(update.message.from_user.first_name + " " + update.message.from_user.last_name)
    except TypeError:
        nom_usuari = str(update.message.from_user.first_name)

    longitud = len(concepte)
    max_admited = 140
    if longitud >= max_admited:
        update.message.reply_text("Com vols que recordi una cosa tan llarga? Puc recordar un twit dels antics (140 caracters)")
    else:
        data = {}
        data["concepte"] = concepte
        data["usuari"] = nom_usuari
        data["data"] = now.strftime("%d/%m/%Y %H:%M:%S")
        data["memoria"] = str(update.message.message_id)

        conceptes_list.append(data)
        print(data)

        missatge = nom_usuari+" m'ha ensenyat: "+'"'+concepte+'"'
        update.message.reply_text(missatge)
        tweet(missatge)