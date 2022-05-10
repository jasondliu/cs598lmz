import lzma
lzma.LZMADecompressor
import warnings
import bz2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import LatentDirichletAllocation as LDA
import nltk 
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tag.stanford import StanfordPOSTagger
import os
from nltk import word_tokenize
import gensim
from gensim import corpora
import pyLDAvis.gensim
import numpy as np
import numpy.linalg as LA
import re
import pandas as pd
import pyLDAvis
import gzip

warnings.filterwarnings("ignore")
pyLDAvis.
