import ctypes
ctypes.cast(None, ctypes.py_object)

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import pathlib
import mne
import scipy
from scipy import signal
import os
import fnmatch
import copy

from sklearn.pipeline import Pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import StratifiedKFold, permutation_test_score
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics
