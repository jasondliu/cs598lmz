import mmap
import cPickle
import sys
import os
import glob
import math
import subprocess
import re
import time
import logging
import argparse

import numpy as np
import scipy.optimize
import scipy.special
import scipy.stats
import scipy.sparse

from multiprocessing import Pool

from sklearn.metrics import roc_curve, auc

from sklearn.linear_model import LogisticRegression


#from sklearn.linear_model import LogisticRegression
#from sklearn.linear_model import LogisticRegressionCV
#from sklearn.linear_model import SGDClassifier
#from sklearn.linear_model import PassiveAggressiveClassifier
#from sklearn.linear_model import Perceptron
#from sklearn.linear_model import RidgeClassifier
#from sklearn.linear_model import RidgeClassifierCV
#from sklearn.linear_model import Lasso
#from sklearn.linear_model import LassoCV
#from sklearn.linear_model import ElasticNet
#from sklearn.linear_
