import threading
threading.stack_size(2**27)
import sys
import re
import os
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from wordcloud import WordCloud
from matplotlib import pyplot as plt

file_dir = os.path.dirname(os.path.dirname(os.path.realpath('__file__')))
mudule_dir = os.path.dirname(os.path.dirname(os.path.realpath('__file__')))
sys.path.insert(0, file_dir + "/DataProcessing/")
from try_es import es_query
