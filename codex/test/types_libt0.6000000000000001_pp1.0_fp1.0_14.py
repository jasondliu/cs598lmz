import types
types.ModuleType.__repr__ = lambda self: self.__name__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_curve, auc

from scipy import interp
from itertools import cycle

import warnings
warnings.filterwarnings('ignore')

