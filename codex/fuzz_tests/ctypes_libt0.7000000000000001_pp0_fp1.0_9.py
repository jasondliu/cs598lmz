import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")
import numpy as np
import pandas as pd
import os
import sys
import datetime
import datetime as dt
from math import ceil
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import warnings
warnings.filterwarnings('ignore')
import openpyxl
import gc
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import f1_score
from
