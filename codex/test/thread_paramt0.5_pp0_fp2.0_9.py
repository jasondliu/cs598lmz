import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

print('TESTING:', __file__)

import os, sys, argparse, time, re, threading, traceback
import numpy as np

from keras import backend as K
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras.optimizers import Adam, SGD

from lib.callbacks import MultiGPUCheckpointCallback
from lib.utils.osutils import mkdir_p
from lib.utils.config_parse import cfg_from_file
from lib.utils.timer import Timer
from lib.utils.multi_gpu_model import multi_gpu_model
from lib.utils.data_augment import data_augment
from lib.utils.data_generator import DataGenerator
from lib.utils.data_generator_inference import DataGeneratorInference

from lib.models.resnet_3D_v1 import resnet_3D_v1, resnet_3D_v1_no_top
