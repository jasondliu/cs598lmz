import threading
threading.stack_size(67108864) # 64MB stack

import os
import sys
import time

import matplotlib
matplotlib.use('Agg')

import numpy as np
import theano

import lasagne
import theano.tensor as T

from constants import *
from data_utils import *
from models import *
from experiment import *

def main(
    # Training/validation paths
	train_data_path = 'data/train.h5',
	valid_data_path = 'data/valid.h5',

	# Training params
	n_epochs           = 6000,
    batch_size         = 20,
    checkpoint_every   = 100, # Save best model
    patience           = 100, # Check model performance every `patience` epochs during training
    disp_every         = 1,
	early_stopping     = True, # Stop when performance on validation set not improving after `patience` epochs

	# Architecture
	arch = 'rnn',

	# Dropout and ensemble model weights/biases
	dropout           =
