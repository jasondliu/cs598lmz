import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b]2;{}\x07".format(sys.argv[1]))).start()

from os.path import join, exists
from os import makedirs
import numpy as np
import json
from tqdm import tqdm
from itertools import product
from sklearn.model_selection import ParameterGrid
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.utils import shuffle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer

from utils import load_data, load_data_from_files
from utils import save_data_to_files, save_data
from utils import generate_features, generate_features_
