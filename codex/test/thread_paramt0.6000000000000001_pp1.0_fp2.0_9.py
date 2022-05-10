import sys, threading
threading.Thread(target=lambda: sys.stdout.write('')).start()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

from IPython.display import HTML
from IPython.display import display

pd.set_option('display.max_columns', None)

import eli5
from eli5.sklearn import PermutationImportance

import shap
shap.initjs()

import folium
from folium.plugins import HeatMap

from tqdm import tqdm

