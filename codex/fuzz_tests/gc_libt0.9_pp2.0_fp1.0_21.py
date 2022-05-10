import gc, weakref
import logging
from sklearn.neighbors import KernelDensity

from joblib import Parallel, delayed
import multiprocessing

from sklearn.externals.joblib import Memory
from sklearn.datasets import load_svmlight_file

from sklearn import grid_search
import sys
from functools import partial

from operator import itemgetter
from heapq import nsmallest
from random import choice
import random
from scipy import stats
from sklearn.metrics import r2_score
import lhsmdu

from scipy.spatial.distance import euclidean
from time import time
from scipy import stats as st
from scipy.stats import kendalltau, pearsonr

from setcoverpy import setcover
from array import *
from scipy.stats import spearmanr
from scipy.stats import entropy

from datetime import datetime, date, time
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import mean_squared_error
from sklearn.
