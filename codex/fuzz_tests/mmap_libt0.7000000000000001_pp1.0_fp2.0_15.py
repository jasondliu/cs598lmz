import mmap
import numpy as np
import pandas as pd
import random

import tensorflow as tf
import tensorflow_ranking as tfr

from tensorflow.python.framework.ops import disable_eager_execution

disable_eager_execution()

tf.compat.v1.enable_eager_execution()

_TRAIN_DATA_PATH = '/home/lucas/PycharmProjects/TCC/data/train_tfrecords'
_TEST_DATA_PATH = '/home/lucas/PycharmProjects/TCC/data/test_tfrecords'
_LISTWISE_DATA_PATH = '/home/lucas/PycharmProjects/TCC/data/listwise_tfrecords'
_CONVOLUTIONAL_DATA_PATH = '/home/lucas/PycharmProjects/TCC/data/convolutional_tfrecords'
_CONVOLUTIONAL_DATA_PATH_ALT = '/home/lucas/PycharmProjects/TCC/data/convolution
