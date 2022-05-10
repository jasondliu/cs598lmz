import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    if "group" in update.message.chat.type:
        bot.sendMessage(update.message.chat_id, text='I\'m a bot, please talk to me!\nUso:   @AvvisiUnictBot')
        return
    bot.sendMessage(update.message.chat_id, text='''Scrivi @AvvisiUnictBot <categoria> <comando> \n\nCategorie:
	News  -  Eventi  -  Didattica  -  A
