import threading
threading.stack_size(2**27)

# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# GPU memory allocation
import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.allow_growth = True

# import keras
import tensorflow.keras as keras

# import keras.backend as K
import tensorflow.keras.backend as K

# import keras.layers as layers
import tensorflow.keras.layers as layers

# import keras.models as models
import tensorflow.keras.models as models

# import keras.optimizers as optimizers
import tensorflow.keras.optimizers as optimizers

# import keras.callbacks as callbacks
import tensorflow.keras.callbacks as callbacks

# import keras.utils as utils
import tensorflow.keras.utils as utils

# import keras.preprocessing.text as text
import tensorflow.keras
