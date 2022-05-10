from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self: b''
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import time
import sys
import os

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline, FeatureUnion, make_pipeline, make_union
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer, MaxAbsScaler, QuantileTransformer
from sklearn.linear_model import LogisticRegression #SGDClassifier,
from sklearn.svm import NuSVC, LinearSVC
from sklearn.metrics.pairwise import cosine_similarity


from sklearn.ensemble import RandomForestClassifier
#from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.pipeline import Pipeline, FeatureUnion, make_pipeline
from sklearn
