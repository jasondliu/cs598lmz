from bz2 import BZ2Decompressor
BZ2Decompressor
from functools import partial
from multiprocessing.pool import Pool
import os
import sys
import tarfile
import tensorflow as tf
from six.moves import urllib
import imageio

# Main slim library
from tensorflow.contrib import slim


# from tensorflow.contrib.slim.nets import inception
# if tf.__version__ == '1.4.0':
#     raise ImportError('Please upgrade your tensorflow installation to v1.4.* or later!')
# elif tf.__version__ == '1.5.0':
#     tf.contrib.framework.get_or_create_global_step = tf.train.get_or_create_global_step
# else:
#     print(tf.__version__)

# image_size = inception.inception_v3.default_image_size


# names = ['InceptionV3']

# Check if the model has already been downloaded, otherwise download it
# Check if the pretrained weights have already been downloaded, otherwise download them.
def check_or_download
