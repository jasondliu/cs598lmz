import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import yaml
import datetime
import random
import sqlite3
import traceback
import gzip
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from anki.storage import Collection
from app import trellotoolkit
from anki import notes, sched
from anki.utils import fieldChecksum, hexifyID, splitFields, intTime, maxID

from pprint import pprint
try:
    from nltk.tokenize import word_tokenize
except ImportError:
    os.system('./nltk.sh')
    from nltk.tokenize import word_tokenize

def add_trello_to_card(trello_obj, card):
    html = trellotoolkit.render_trello_as_html(trello_obj)
