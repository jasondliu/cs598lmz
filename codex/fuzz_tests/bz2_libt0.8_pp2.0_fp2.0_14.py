import bz2
bz2.BZ2File.__init__ = do_nothing
import sys, re
from numpy import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.stem.porter import *
from nltk.stem.wordnet import *
from nltk.stem.snowball import *
from nltk.stem.porter import *
from collections import Counter
import math
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os, re, sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk, string
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import *
from collections import Counter
import math

ps = PorterStemmer()

def get_lemma(word):
    lemma
