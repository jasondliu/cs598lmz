from lzma import LZMADecompressor
LZMADecompressor()
from pprint import pprint
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)
import re
from gensim.models import Word2Vec
from bs4 import BeautifulSoup
import urllib3
from clickbait_model import clickbait_model

urllib3.disable_warnings()
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
wordnet_lemmatizer = WordNetLemmatizer()
stemmer = SnowballStemmer('english')
# import
