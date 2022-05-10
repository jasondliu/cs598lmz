import threading
threading.stack_size(2**27)
import sys
import gc
import numpy as np
from scipy import stats
import pickle
import pandas as pd
import time
start_time = time.time()
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits
from sklearn.manifold import TSNE
from sklearn.datasets import load_iris, load_digits
from sklearn.decomposition import PCA

import xgboost as xgb
from sklearn.model_selection import GridSearchCV

# Model to predict interactions
from sklearn.ensemble import RandomForestClassifier

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Set some parameters to get good visuals - style to ggplot and size to 15,10
pd.set_option('display.precision',4)

%matplotlib inline
