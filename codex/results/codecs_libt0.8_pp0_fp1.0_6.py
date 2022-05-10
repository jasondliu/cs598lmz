import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import sys
import json
import re
from os.path import expanduser, join
import simplejson
import subprocess
from multiprocessing import Pool
from collections import defaultdict
from collections import Counter
from pprint import pprint
import subprocess
import fractions, decimal

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk import pos_tag
from nltk.corpus.reader.wordnet import VERB
from nltk.corpus.reader.wordnet import ADJ
from nltk.corpus.reader.wordnet import NOUN
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer

from autocorrect import spell

from gensim import corpora, models, similarities
