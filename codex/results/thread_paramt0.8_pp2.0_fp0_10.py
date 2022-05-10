import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'*80)).start()
import numpy as np
import time
import os
import argparse
import shutil

import torch
import torch.utils.data as data
import torch.backends.cudnn as cudnn

import _init_paths
import models
from config import cfg
from config import update_config
from utils.utils import create_logger
from utils.transforms import *
from utils.datasets import *
from utils.utils import *


def parse_args():
    parser = argparse.ArgumentParser(description='Train keypoints network')
    # general
    parser.add_argument('--cfg', default='experiments/coco/hrnet/w32_256x192_adam_lr1e-3.yaml', type=str, help='experiment configure file name')
    parser.add_argument('--use-tensorboard', action='store_true', default=False, help='whether use tensorboard')
    parser.add_argument('opts', nargs=argparse
