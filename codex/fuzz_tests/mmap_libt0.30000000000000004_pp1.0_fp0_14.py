import mmap
import numpy as np
import os
import sys
import time

import tensorflow as tf
from tensorflow.python.platform import gfile

from tensorflow.python.platform import app
from tensorflow.python.platform import flags

from tensorflow.python.util import compat

FLAGS = flags.FLAGS

tf.logging.set_verbosity(tf.logging.INFO)

def _int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def _bytes_feature(value):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _convert_to_example(filename, image_buffer, label, text, height, width):
  colorspace = 'RGB'
  channels = 3
  image_format = 'JPEG'

  example = tf.train.Example(features=tf.train.Features(feature={
      'image/height': _int64_feature(height),

