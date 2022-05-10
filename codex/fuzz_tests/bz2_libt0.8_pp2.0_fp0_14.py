import bz2
bz2.__version__

from bz2 import BZ2File
import os
from os.path import join, exists, isdir, dirname
from os import makedirs
import pandas as pd
import numpy as np
import regex as re
from collections import Counter, defaultdict
from glob import glob
from itertools import chain, combinations
from tqdm import tqdm
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import TruncatedSVD, NMF
from sklearn.cluster import KMeans
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_selection import SelectKBest, chi2, VarianceThreshold
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, average_precision_score, precision_recall_curve
from sklearn.base
