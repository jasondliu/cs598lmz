import codecs
codecs.register_error('txtencode', lambda ex: (u'',ex.end))
from collections import Counter
from lxml import etree
import dateutil
import dateutil.rrule as drr
from string import punctuation
from textblob import TextBlob
from textblob import Word
import os
import re
from collections import defaultdict
from itertools import groupby
import cPickle as pickle


stop = set(stopwords.words('english'))
stop.update(['gt', 'gonna', 'p', 'edu', 'w', 'org', 'com', 'html', 'net', 'et', 'al', 'j', 'co', 'cgi', 'web', 'cfm', 'asp', 'www', 'php', 'htm', 'calendar', 'default', 'asp'])

def remove_stopwords(text):
    return [word for word in text if word not in stop]

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


