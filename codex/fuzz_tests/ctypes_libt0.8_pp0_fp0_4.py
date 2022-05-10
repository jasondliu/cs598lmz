import ctypes
ctypes.CDLL('libc.so.6', ctypes.RTLD_GLOBAL)

import tensorflow as tf
from keras.models import Sequential, load_model
from keras.layers import LSTM, TimeDistributed, Activation, Dense, Dropout, Masking, Input
from keras.optimizers import Adam
from keras import backend as K
from keras.utils import multi_gpu_model
from keras.callbacks import ModelCheckpoint
from keras.models import Model, load_model
from keras.utils import plot_model
from keras.regularizers import l2
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.layers import Conv1D, MaxPooling1D
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.embeddings import Embedding
from keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler, MinMaxScaler
