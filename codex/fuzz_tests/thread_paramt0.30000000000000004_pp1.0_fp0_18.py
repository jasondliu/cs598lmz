import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import tensorflow as tf
from tensorflow.contrib.slim.nets import inception

import inception_preprocessing
from inception_resnet_v2 import inception_resnet_v2, inception_resnet_v2_arg_scope

slim = tf.contrib.slim

tf.flags.DEFINE_string(
    'master', '', 'The address of the TensorFlow master to use.')

tf.flags.DEFINE_string(
    'checkpoint_path', '/tmp/tfmodel/',
    'The directory where the model was written to or an absolute path to a '
    'checkpoint file.')

tf.flags.DEFINE_string(
    'test_image_path', '', 'Test image path')

tf.flags.DEFINE_integer(
    'num_classes', 1001, 'Number of classes.')

tf.flags.DEFINE_integer(
    'labels_offset', 0,
    'An offset for the
