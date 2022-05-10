from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('train.ft.txt.bz2').read())

import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

nltk.download('stopwords')
nltk.download('wordnet')
stopwords_english = stopwords.words('english')
stemmer = PorterStemmer()

def preprocess(tweet):
    tweet = tweet.lower()
    tweet = re.sub('\[.*?\]', '', tweet)
    tweet = re.sub('https?://\S+|www\.\S+', '', tweet)
    tweet = re.sub('<.*?>+', '', tweet)
    tweet = re.sub('[%s]' % re.escape(string.punctuation), '', tweet)
    tweet = re.sub('\n', '', tweet)
    tweet = re.sub('\w*\d\w*', '', tweet)
    tweet =
