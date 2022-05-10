import threading
threading.stack_size(2**27)
import sys
import pygame
import os
from pygame.locals import *
from random import randint
from random import shuffle
import time
import random
import numpy as np
import cv2
import pickle
import copy
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow.contrib.slim as slim
import scipy.signal
import csv
import cv2

from helper import *
from vizdoom import *

# Copies one set of variables to another.
# Used to set worker network parameters to those of global network.
def update_target_graph(from_scope,to_scope):
    from_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, from_scope)
    to_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, to_scope)

    op_holder = []
    for from_var,to_var in zip(from_v
