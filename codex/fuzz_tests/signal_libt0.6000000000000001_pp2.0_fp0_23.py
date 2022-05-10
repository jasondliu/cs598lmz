import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
sys.path.append('/home/ubuntu/workspace/utils')
sys.path.append('/home/ubuntu/workspace/video_prediction')

import argparse
import numpy as np
import scipy.misc
import tensorflow as tf
import random
import os

from data_reader import DataReader
from image_utils import *
from video_prediction import VideoPredictionModel
from tensorflow.python.framework import ops

# define global parameters
FLAGS = flags.FLAGS
flags.DEFINE_string('checkpoint_dir', '/home/ubuntu/workspace/video_prediction/checkpoint/',
                    'Directory to load model checkpoints.')
flags.DEFINE_string('dataset_dir', '/home/ubuntu/workspace/video_prediction/data/',
                    'Directory to load datasets.')
flags.DEFINE_string('output_dir', './output',
                    'Directory to save output.')
flags.DEFINE_integer('
