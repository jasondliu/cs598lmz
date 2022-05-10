import socket
socket.gethostname()

import os
import sys
nb_dir = os.path.split(os.getcwd())[0]
if nb_dir not in sys.path:
    sys.path.append(nb_dir)

import numpy as np
import pandas as pd
import seaborn as sns

from scipy.stats import pearsonr
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

from modules.factorial_analysis import plot_factorial_plane
from modules.factorial_analysis import plot_correlation_matrix
from modules.factorial_analysis import plot_scree_plot
from modules.factorial_analysis import normalize_data

from modules.utils import print_full_dataframe

from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_
