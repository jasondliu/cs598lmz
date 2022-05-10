import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['axes.titlesize'] = 'large'

import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['axes.titlesize'] = 'large'

import warnings
warnings.filterwarnings('ignore')

#https://www.kaggle.com/c/home-credit-default-risk
