import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import multiprocessing as mp
import time
import datetime
import os
import sys

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

if 'DISPLAY' not in os.environ:
    plt.switch_backend('Agg')

from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, TerminateOnNaN
from keras import backend as K
from keras.models import load_model
from math import ceil
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
from keras.models import load_model

from models.keras_ssd7 import build_model
from keras_loss_function.keras_ssd_loss import SSDLoss
from keras_layers.keras_layer_AnchorBoxes import AnchorBoxes
from keras_layers.keras_layer_DecodeDetections import Dec
