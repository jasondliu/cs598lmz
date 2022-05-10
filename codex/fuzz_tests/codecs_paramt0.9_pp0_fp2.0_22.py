import codecs
codecs.register_error('replace_ligatures', lambda err: (u'', err.start + 1))

from gensim import corpora, models, similarities, matutils
from collections import defaultdict
from pprint import pprint  # pretty-printer
from six import iteritems, itervalues
from six.moves import zip, range
from smart_open import smart_open
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk import PorterStemmer
import re
from datetime import datetime
import os
import csv


def iter_documents(top_directory):
    """Iterate over all documents, yielding a document (=list of utf8 tokens) at a time."""
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.html'), files):
            document = read_document(os.path.join(root, file))  # read the bytes data from the file
            if len(document) >= MIN_LENGTH:  # yield lists of tokens
                yield document
