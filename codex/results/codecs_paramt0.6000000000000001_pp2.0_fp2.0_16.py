import codecs
codecs.register_error('ignore', codecs.lookup_error('ignore'))
import re
import os
import sys
import string
import numpy as np
import scipy.sparse
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics import mean_squared_error
from sklearn.decomposition import NMF
import pandas as pd
import nltk
import nltk.stem
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import Tfid
