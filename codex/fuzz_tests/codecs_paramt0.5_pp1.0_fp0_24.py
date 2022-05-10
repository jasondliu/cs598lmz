import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))

#import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches
#import matplotlib.dates as mdates
#import matplotlib.ticker as ticker

#import datetime
#import time
#import calendar
#import os

#from operator import itemgetter
#from collections import defaultdict

#from pandas import DataFrame, Series

#from numpy import arange, array, ones

#import pylab

#from sklearn import preprocessing
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.decomposition import PCA

import numpy as np
import pandas as pd

from scipy import sparse

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
