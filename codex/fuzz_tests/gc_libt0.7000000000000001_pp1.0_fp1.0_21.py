import gc, weakref
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml
import re
import os

import time
import datetime
import locale

from fastai.vision.data import ImageList
from fastai.vision.transform import get_transforms
from fastai.vision.data import ImageDataBunch
from fastai.vision.learner import create_cnn
from fastai.metrics import error_rate, accuracy

from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, fbeta_score, accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, auc
import seaborn as sns

import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='torch.utils.data')
 
%matplotlib inline
 
# %reload_ext autoreload
# %autoreload 2
# %matplotlib
