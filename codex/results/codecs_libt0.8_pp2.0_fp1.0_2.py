import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from scipy import stats
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

plt.style.use('ggplot')
#pd.options.display.max_columns = 99
pd.options.display.max_rows = 99

def warn(*args, **kwargs): pass
import warnings
warnings.warn = warn
 

import seaborn as sns
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold

