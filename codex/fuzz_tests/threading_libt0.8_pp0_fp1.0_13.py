import threading
threading.stack_size(2**27)
import sys
import tensorflow as tf
import pickle
import numpy as np
import time
import os

LOCAL_DOWNLOAD_FOLDER = os.getcwd() + "/local_download_folder"

if not os.path.exists(LOCAL_DOWNLOAD_FOLDER):
    os.makedirs(LOCAL_DOWNLOAD_FOLDER)

from game_ac_network import GameACFFNetwork, GameACLSTMNetwork
from a3c_training_thread import A3CTrainingThread
from rmsprop_applier import RMSPropApplier

from constants import ACTION_SIZE
from constants import PARALLEL_SIZE
from constants import INITIAL_ALPHA_LOW
from constants import INITIAL_ALPHA_HIGH
from constants import INITIAL_ALPHA_LOG_RATE
from constants import MAX_TIME_STEP
from constants import CHECKPOINT_DIR
from constants import LOG_FILE
from constants import RMSP_EPSILON
from constants import RMSP_
