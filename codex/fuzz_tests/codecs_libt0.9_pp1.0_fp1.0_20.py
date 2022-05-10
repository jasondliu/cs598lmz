import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams
from matplotlib import cm as cm
import seaborn as sns
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from scipy import stats

#######机器学习#######
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, roc_auc_score,precision_score,recall_score,f1_score
from sklearn
