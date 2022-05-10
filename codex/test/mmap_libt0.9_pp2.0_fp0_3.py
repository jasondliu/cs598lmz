import mmap
import struct
import time
import sys
import numpy as np
import cv2
#import matplotlib
#matplotlib.use('GTKAgg')
#import pylab as plt

# ============== ADDED BY ALEX ==============
import os
import glob
import read_scene_functions as rdf
# ===========================================

# ============== TRAINING ==============
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import (StratifiedKFold, ParameterGrid,
									 cross_val_score)
from sklearn.metrics import (precision_score, recall_score, roc_curve,
							 precision_recall_curve, roc_auc_score)
from sklearn.utils import shuffle
from sklearn.svm import SVC
# ======================================

DEFAULT_PALETTE = 'jet'
DEFAULT_PEAKS = '(0,1,2)'
DEFAULT_TRAINING_INDEX
