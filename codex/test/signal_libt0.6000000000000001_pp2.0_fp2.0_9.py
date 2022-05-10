import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
import sys
from multiprocessing import Queue
import time
from collections import namedtuple
from random import random

from rss_parser import RssParser
from reddit_parser import RedditParser
from news_api_parser import NewsApiParser
from twitter_parser import TwitterParser
from db_manager import DbManager
from text_processor import TextProcessor
from news_fetcher import NewsFetcher
from twitter_fetcher import TwitterFetcher
from main_window import MainWindow
from news_processor import NewsProcessor
from twitter_processor import TwitterProcessor
from twitter_analyzer import TwitterAnalyzer
from news_analyzer import NewsAnalyzer
from news_corpus import NewsCorpus
from twitter_corpus import TwitterCorpus

