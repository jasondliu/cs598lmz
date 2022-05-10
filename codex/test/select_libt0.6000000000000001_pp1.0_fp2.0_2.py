import selectors
import sys
from time import time

from datetime import datetime
from urllib.parse import urlparse
from aiohttp import web
from aiohttp import ClientSession
from aiohttp_socks import SocksConnector, ProxyType
from bs4 import BeautifulSoup
from bs4.element import Comment
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from redis import Redis

from .settings import *

stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

EXIT_CODE = 0


