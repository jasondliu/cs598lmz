import mmap
import numpy as np
import os
import random
import re
import sys
import time
import unicodedata
import zipfile

from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf

from tensorflow.python.ops import math_ops
from tensorflow.python.ops import nn_ops
from tensorflow.python.ops import array_ops

# from tensorflow.python.ops import variable_scope as vs

# from tensorflow.models.rnn.translate import data_utils
# from tensorflow.models.rnn.translate import seq2seq_model

import data_utils
import seq2seq_model

tf.app.flags.DEFINE_float("learning_rate", 0.5, "Learning rate.")
tf.app.flags.DEFINE_float("learning_rate_decay_factor", 0.99,
                          "Learning rate decays by this much.")
tf.app.flags.DEFINE_float("max
