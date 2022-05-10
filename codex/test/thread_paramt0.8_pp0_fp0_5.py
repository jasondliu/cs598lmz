import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()

# import faulthandler
# faulthandler.enable()

import os
import time
import argparse
import numpy as np
import tensorflow as tf
import uabDataReader
import uabRepoPaths
import bohaoCustom.uabPreprocClasses as bPreproc

import uabCrossValMaker
import uab_collectionFunctions
from bohaoCustom import uabMakeNetwork_UNet

RUN_ID = 0
BATCH_SIZE = 5
LEARNING_RATE = 5e-5
INPUT_SIZE = 572
TILE_SIZE = 5000
EPOCHS = 100
NUM_CLASS = 2
N_TRAIN = 8000
N_VALID = 1000
GPU = 0
DECAY_STEP = 80
DECAY_RATE = 0.1
MODEL_NAME = 'inria_aug_grid_{}'
SFN = 32
ZERO_MASK_THRESHOLD = 0.35
