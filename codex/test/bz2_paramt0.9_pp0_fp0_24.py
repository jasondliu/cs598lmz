from bz2 import BZ2Decompressor
BZ2Decompressor()

import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

import pickle

from nltk.corpus import stopwords 
stop_words = set(stopwords.words('english'))


path = "/content/drive/My Drive/FINAL YEAR/collection.json.bz2"
