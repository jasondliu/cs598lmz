import select
import sys
import re
import time
import os
import pdb
import json
import random
import argparse
import threading

import numpy as np

import tensorflow as tf
from tensorflow.contrib.rnn import LSTMCell, MultiRNNCell, DropoutWrapper
from tensorflow.contrib.layers import xavier_initializer as xav

import utils

class ChatBotModel(object):
    def __init__(self, FLAGS, id2line, word2id):
        print('Initialize new model')
        self.FLAGS = FLAGS
        self.id2line = id2line
        self.word2id = word2id

        self.buckets = [(5, 10), (10, 15), (20, 25), (40, 50)]
        self.PAD_ID = 0
        self.GO_ID = 1
        self.EOS_ID = 2
        self.UNK_ID = 3

        self.learning_rate = FLAGS.learning_rate
        self.learning_rate
