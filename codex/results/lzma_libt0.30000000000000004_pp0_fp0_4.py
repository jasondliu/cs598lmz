import lzma
lzma.open

import os
import sys
import time
import random
import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
import gc
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.preprocessing import LabelEncoder
from scipy.stats import spearmanr
from scipy.stats import rankdata
from scipy.stats import pearsonr
from scipy.stats import kendalltau
from scipy.stats import norm
from scipy.special import softmax
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import PCA
from sklearn.decomposition import SparsePCA
from sklearn.decomposition import NMF
from sklearn.decomposition import FastICA
from sklearn
