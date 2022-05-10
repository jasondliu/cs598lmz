import codecs
codecs.register(lambda name: codecs.lookup('utf8')
 if name == 'utf8mb4' else None)

from classify import classify
from Bot_DB import *
from visualizations import *
from Translations import *
from classifier_vectors import *


# Instantiate our bot
app = Flask(__name__)
bot = Bot(os.environ['BOT_KEY'])

default_keyboards = {
        u'English': ['There', 'is', 'a', 'graveyard', 'at', 'the', 'end', 'of', 'the', 'world'],
        u'German' : ['Hier', 'ist', 'ein', 'Friedhof', 'am', 'Ende', 'der', 'Welt'],
        u'Russian': ['Здесь', 'есть', 'кладбище', 'в', 'конце', 'света'],
        u'French' : ['Il', 'y', 'a', 'un', 'cimetiere', 'a
