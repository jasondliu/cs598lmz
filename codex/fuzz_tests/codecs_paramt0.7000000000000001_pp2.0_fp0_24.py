import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)
from html.parser import HTMLParser
import re
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import string
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def remove_punctuation(text):
    words = nltk.word_tokenize(text)
    punctuation_filtered = [w for w in words if w.lower() not in string.punctuation]
    return " ".join(punctuation_filtered)

def remove_stopwords(text):
    words = nltk
