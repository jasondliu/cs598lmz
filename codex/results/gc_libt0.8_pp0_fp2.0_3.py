import gc, weakref
from math import log
import os, re, sys
from json import load as json
from io import StringIO
from collections import defaultdict
from operator import itemgetter
from pprint import pformat
from six.moves import urllib
from six import iteritems
from bs4 import BeautifulSoup
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer


class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass
    def close(self):
        self.terminal.flush()
        self.log.close()

sys.stdout = Logger('log.txt', sys.stdout)
sys.stderr = Logger('log.txt', sys.stderr
