import threading
threading.stack_size(268435456)

import tensorflow as tf
import numpy as np
import os
import sys
import time
import logging
import scipy.misc
import cv2
import random
import copy
import itertools
import re

# from tensorflow.python.client import device_lib
# device_lib.list_local_devices()

from utils import *
from model import *
from data_loader import *
from loss import *


'''
  Training script for the following paper
  "Joint Motion Prediction and Behavior Cloning using Trajectory-conditioned Deep Dynamical Models"
  by Yan Duan, Xi Chen, Rein Houthooft, John Schulman, Pieter Abbeel
  International Conference on Learning Representations (ICLR), 2017
  https://arxiv.org/abs/1611.03897
'''

# def softmax(x):
#     """Compute softmax values for each sets of scores in x."""
#     e_x = np.exp(x - np.max(x))
#
