from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import logging

youtube_url = "https://www.youtube.com/feeds/videos.xml?channel_id=UCDhM2k2Cua-JdobAh5moMFg"
html = requests.get(youtube_url)
soup = BeautifulSoup(html.content, 'lxml')

all_videos = soup.find_all("entry")
all_links = []

for entries in all_videos:
    # for title in entries.find_all("title"):
    #     all_links.append(title.text)
    for link in entries.find_all("link"):
        all_links.append(link["href"])

new_list = ', '.join(all_links[0:3])
print(new_list)

updater = Updater(token='1780866236:AAFX0dSVEneQNj0THtSbkFgdAKPV_zH8foU', use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello MIDZY! Looking for updates?")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# get updates from the link
def get_updates(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hey MIDZY, watch these 3 new videos: " + new_list)

updates_handler = CommandHandler('get_updates', get_updates)
dispatcher.add_handler(updates_handler)

updater.start_polling()

# note that the link for get_updates changes everytime the script is run
