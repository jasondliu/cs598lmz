import mmap
import os
import re
import sys
import time

import numpy as np
import tensorflow as tf

from tensorflow.python.platform import gfile
from tensorflow.python.platform import tf_logging as logging
from tensorflow.python.util import compat

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string('input_dir', '',
                           'Directory to put the input data.')
tf.app.flags.DEFINE_string('output_dir', '',
                           'Directory to put the output data.')
tf.app.flags.DEFINE_string('start_word', '<S>',
                           'Special word added to the beginning of each sentence.')
tf.app.flags.DEFINE_string('end_word', '</S>',
                           'Special word added to the end of each sentence.')
tf.app.flags.DEFINE_string('unknown_word', '<UNK>',
                           'Special word meaning unknown.')
tf.app.flags.DEFINE_integer
