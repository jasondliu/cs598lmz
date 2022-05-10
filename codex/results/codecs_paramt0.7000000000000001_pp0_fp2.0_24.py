import codecs
codecs.register_error('strict', codecs.ignore_errors)
import sys
import pickle
import gzip
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation, Input, LSTM, Embedding
from keras.layers.normalization import BatchNormalization
from keras.optimizers import SGD, RMSprop, Adadelta
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.utils import np_utils
from keras import backend as K
from keras.utils.visualize_util import plot
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib
from sklearn import metrics
import matplotlib.py
