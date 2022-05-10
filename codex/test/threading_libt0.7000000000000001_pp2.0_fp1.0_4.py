import threading
threading.stack_size(67108864)

import time
import os
import numpy as np
import tensorflow as tf

from config import Config
from model import Model
from train import train
from test import test

# commented out so that the program is able to run without
# the tensorflow debugger
#from tensorflow.python import debug as tf_debug

class OthelloConfig(Config):
    """Othello game related config."""
    def __init__(self):
        super(OthelloConfig, self).__init__()

        # game-related
        self.board_size = 8
        self.action_size = self.board_size**2
        self.in_channels = 17 # 8 + 1 + 8
        self.num_classes = 1

        # training-related
        self.batch_size = 128
        self.eval_batch_size = 256
        self.resign_threshold = -0.98
        self.num_eval_games = 500
        self.learning_rate_init = 1e-4
