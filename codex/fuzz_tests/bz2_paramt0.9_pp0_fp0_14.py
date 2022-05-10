from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self: b''

# Tensorflow modules
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.applications import imagenet_utils
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.applications.imagenet_utils import decode_predictions, _obtain_input_shape
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.layers import Input, Conv2D, MaxPooling2D, AveragePooling2D, ZeroPadding2D, Concatenate,Flatten,Activation,Dense, Dropout
from tensorflow.python.keras.models import Sequential, Model
from tensorflow.python.keras.utils import plot_model, to_categorical
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.applications.imagenet_utils import preprocess_input
from tensorflow.python.keras
