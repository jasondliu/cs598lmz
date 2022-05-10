import threading
threading.stack_size(2**27)

import sys
import time
import random
import math
import os
import numpy as np

import tensorflow as tf
import tensorflow.contrib.layers as layers
import tensorflow.contrib.slim as slim
import tensorflow.contrib.rnn as rnn
import tensorflow.contrib.distributions as distributions

from game_ac_network import GameACFFNetwork, GameACLSTMNetwork
from a3c_training_thread import A3CTrainingThread
from rmsprop_applier import RMSPropApplier

from constants import ACTION_SIZE
from constants import PARALLEL_SIZE
from constants import CHECKPOINT_DIR
from constants import RMSP_EPSILON
from constants import RMSP_ALPHA
from constants import GRAD_NORM_CLIP
from constants import USE_GPU
from constants import USE_LSTM
from constants import USE_DIST
from constants import USE_LSTM_DIST
from constants import USE_LSTM_DIST_SEPARATE
