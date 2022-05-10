import types
types.ModuleType.__repr__ = lambda self: self.__name__

import tensorflow as tf

from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Conv2D, Dropout, Activation, Flatten, Dense, MaxPooling2D, ZeroPadding2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import backend as K

train_data_dir = './train'
validation_data_dir = './validation'

train_samples = 2000
validation_samples = 800

epochs = 50
batch_size = 16

img_width, img_height = 150, 150

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height
