import mmap
import shelve

from collections import defaultdict
from itertools import product, repeat
from random import randint
from random import shuffle
from random import sample
from time import time

from numpy.random import choice
from numpy.random import shuffle as np_shuffle

from nltk.corpus import wordnet as wn

from resolve_ngrams import resolve_ngrams

from utils import get_bigrams

from utils import make_bigram_dataset as mbd

from utils import get_similarities

from utils import get_categories as get_categories_

from utils import get_categories_from_corpus

from utils import shuffle_dataset

from utils import get_words_and_categories

from utils import word2vec_model_path

from utils import make_word2vec_model as mwm

from utils import get_categories_from_wiki

from utils import get_categories_from_wiki_

from utils import get_categories_from
