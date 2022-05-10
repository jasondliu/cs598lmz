import threading
threading.stack_size(1024*1024)

import sys
sys.path.insert(0, './')

import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"

import numpy as np
import tensorflow as tf
import random
from tensorflow.python.client import timeline
from tensorflow.python.profiler import model_analyzer
from tensorflow.python.profiler import option_builder

from train import FLAGS
from train import train_step
from train import validation_step
from train import get_learning_rate
from train import get_loss
from train import get_optimizer
from train import get_train_op
from train import get_dataset
from train import get_model
from train import get_checkpoint
from train import get_checkpoint_manager
from train import get_summary_writer
from train import get_summary_op
from train import get_train_log_dir
from train import get_validation_log
