import codecs
codecs.register_error("strict", codecs.ignore_errors)

from pandas import DataFrame
from os import listdir
from os.path import isfile, join
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
import gensim
from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec
from gensim import models
from matplotlib import pyplot
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.svm import SVC
import pickle
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.
