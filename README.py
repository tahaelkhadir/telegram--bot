# telegram--bot
# by cossmose
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Fonction de gestion de la commande /start
def start(update, context):
    update.message.reply_text("Bienvenue! Je suis un chatbot simple.")

# Fonction de gestion des messages texte
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Mettez votre token Telegram ici
    TOKEN = "votre_token"

    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # Ajouter des gestionnaires de commandes et de messages
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Démarrer le bot
    updater.start_polling()

    # Garder le programme en cours d'exécution jusqu'à ce que l'utilisateur appuie sur Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
              
