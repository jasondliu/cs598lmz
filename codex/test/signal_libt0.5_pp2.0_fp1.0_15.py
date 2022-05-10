import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time
import logging
import numpy as np
import pandas as pd
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

#
#   logging
#
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    stream=sys.stdout)

#
#   constants
#

#
#   functions
#
def train(input_file_path, model_file_path, epochs):
    """
    """
    #
    #   read data
    #
