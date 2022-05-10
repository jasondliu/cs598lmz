import ctypes
ctypes.cast(0, ctypes.py_object).value = None

# this is needed for matplotlib to work in virtual environments
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
import os
import sys
import logging
import argparse
import random
import cv2
import time

# todo: change this to be relative
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from src.utils.train_utils import get_model_name
from src.utils.train_utils import save_checkpoint
from src.utils.train_utils import load_checkpoint
from src.utils.train_utils import load_pretrained_model
from src.utils.train_utils import load_dataset
from src.utils.train_utils import get_optimizer
from src.utils.train_utils import get_scheduler
from src.utils.train_utils import get_loss_function
from src.utils.train_utils import get_metric
