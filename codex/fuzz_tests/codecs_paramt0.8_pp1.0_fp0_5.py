import codecs
codecs.register_error('ignore_error', codecs.lookup_error('ignore'))
from bs4 import BeautifulSoup
import re
import os
from whoosh.index import create_in,open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser
import re
from whoosh import scoring
from whoosh.scoring import BM25F
from whoosh.scoring import TF_IDF
from whoosh.scoring import Frequency
from whoosh.scoring import BM25
from whoosh import qparser
from whoosh.lang.porter import stem
import numpy as np
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.util import ngrams
from n
