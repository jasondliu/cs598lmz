import mmap
import re
from collections import Counter

# third-party library
import gensim
from gensim import corpora
from gensim.models import Word2Vec
from gensim.test.utils import common_texts, get_tmpfile

from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.decomposition import TruncatedSVD

from pprint import pprint

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

from collections import Counter

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


