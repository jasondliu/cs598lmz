import mmap, time
import subprocess

#from scipy.io import savemat
from scipy.io import loadmat

from keras.layers import Input, Dense, Convolution1D, MaxPooling1D, UpSampling1D, Flatten, Reshape, Dropout, merge, Embedding
from keras.layers.convolutional import Convolution2D, MaxPooling2D, UpSampling2D
from keras.layers.normalization import BatchNormalization
from keras.models import Model
from keras.layers.core import Activation
from keras.callbacks import TensorBoard
from keras.optimizers import Adadelta, RMSprop, adam
from keras.layers.advanced_activations import LeakyReLU, PReLU
from keras.layers import Input, Dense, Convolution1D, MaxPooling1D, UpSampling1D, Flatten, Reshape, Dropout, merge, Embedding
from keras.layers.convolutional import Convolution2D, MaxPooling2D,
