import codecs
codecs.register_error("replace_with_space", lambda e: (u" ", e.start + 1))

# Printing
from pprint import pprint

# Matplotlib drawing
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Preprocessing
from nltk.tokenize import RegexpTokenizer
from nltk  import ngrams
from nltk.corpus import stopwords
from numpy import *
import community
import networkx as nx
import math

# Dimensionality reduction
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA

def load_doc(filename):
    # Open the file as read only
    file = open(filename, 'r', errors='replace_with_space')
    # Read all text
    text = file.read()
    # Close the file
    file.close()
    return text

def clean_doc(doc
