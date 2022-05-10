import codecs
codecs.register_error('strict', codecs.ignore_errors)

from collections import defaultdict
from itertools import chain
from math import log
from operator import itemgetter
from os.path import join

from nltk.corpus.reader.wordnet import WordNetError
from nltk.corpus.reader.wordnet import WordNetCorpusReader
from nltk.corpus.reader.wordnet import NOUN, VERB, ADJ, ADV
from nltk.corpus.reader.wordnet import Synset
from nltk.corpus.reader.wordnet import Lemma
from nltk.corpus.reader.wordnet import ADJ_SAT
from nltk.corpus.reader.wordnet import POS_LIST as WN_POS_LIST

from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic

from nltk.corpus.reader.api import CorpusReader
from nltk.corpus.reader.api import CategorizedCorpusReader


