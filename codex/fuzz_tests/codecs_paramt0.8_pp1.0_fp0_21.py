import codecs
codecs.register_error('skip', lambda x: (None, x.start + 1))

from numpy import median, percentile

from spacy.en import English
from spacy.parts_of_speech import NOUN, VERB, ADV, ADJ

from common import *

from pprint import pprint

from multiprocessing import Pool

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from lxml.html import fromstring
from requests import get

from textblob import TextBlob as tb

from pattern.en import parsetree, tag, parse, Sentence

from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from pymongo import TEXT

import pymongo

from datetime import datetime
from dateutil.parser import parse

from collections import defaultdict
from collections import Counter

from unidecode import unidecode

from afinn import Afinn
from textstat.textstat import textstat
from nltk.corpus import wordnet as
