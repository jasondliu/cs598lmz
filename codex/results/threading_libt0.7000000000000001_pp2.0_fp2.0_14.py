import threading
threading.stack_size(2000000000)


import logging, sys, time

def setup_logger():
    logger = logging.getLogger("svhn")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


logger = setup_logger()

import numpy as np

from tqdm import tqdm

from keras.utils import np_utils

from keras.utils.np_utils import to_categorical

from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Flatten, Lambda, Activation
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D, GlobalAveragePooling2D
