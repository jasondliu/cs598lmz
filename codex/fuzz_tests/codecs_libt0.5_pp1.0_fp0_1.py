import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis, skew
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

%matplotlib inline

plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (16.0, 8.0)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', -1)

# train = pd.read_csv('../input/train.csv')
test = pd.read_csv('../input/test.csv')
#
