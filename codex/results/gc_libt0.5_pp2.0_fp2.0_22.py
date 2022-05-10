import gc, weakref
import numpy as np
import random
import time

import tensorflow as tf
import tensorflow.contrib.slim as slim

import math
import os
import sys

import cv2

from collections import deque

from network import *

from utils import *

def train(env, args):
    tf.reset_default_graph()

    # Create network
    with tf.device("/cpu:0"):
        global_step = tf.Variable(0, name='global_step', trainable=False)

        # Get state
        state = tf.placeholder(tf.float32, shape=[None, 84, 84, 4])

        # Get policy
        policy, value = network(state)

        # Get action
        action_size = env.action_size
        action = tf.placeholder(tf.float32, shape=[None, action_size])

        # Get advantage
        advantage = tf.placeholder(tf.float32, shape=[None, 1])

        # Get target value
        target_value = tf.placeholder(tf.
