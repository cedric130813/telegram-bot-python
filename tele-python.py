import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
updater = Updater(token=<TOKEN>, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello there MIDZY!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


# says goodbye
def bye(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="goodbye MIDZY")


bye_handler = CommandHandler('bye', bye)
dispatcher.add_handler(bye_handler)


# whoismybias
def whoismybias(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Yuna is your bias")


bias_handler = CommandHandler('whoismybias', whoismybias)
dispatcher.add_handler(bias_handler)


# sendPhoto
def sendPhoto(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open("chaeshook.jpg", 'rb'),
                           caption=None)


photo_handler = CommandHandler('sendPhoto', sendPhoto)
dispatcher.add_handler(photo_handler)


#YejiPhoto
def YejiPhoto(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=(
                               "https://64.media.tumblr.com/8e6f9942ac07524588405407b4a2c8d6"
                               "/tumblr_plvc6hVD4i1w7pgvx_540.jpg"),
                           caption=None)


yejiphoto_handler = CommandHandler('YejiPhoto', YejiPhoto)
dispatcher.add_handler(yejiphoto_handler)

#sends a gif of Yuna
def YunaGIF(update, context):
    context.bot.send_animation(chat_id=update.effective_chat.id,
                               animation=open("yuna_gif.gif", 'rb')).animation

yunagif_handler = CommandHandler('YunaGIF', YunaGIF)
dispatcher.add_handler(yunagif_handler)

#mimics the GIF you send
#echoGIF
def echoGIF(update, context):
    context.bot.send_animation(chat_id=update.effective_chat.id, animation=update.message.animation)

echoGIF_handler = MessageHandler(Filters.animation & (~Filters.command), echoGIF)
dispatcher.add_handler(echoGIF_handler)
