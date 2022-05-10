import threading
threading.stack_size(1024*1024*8)
import sys
sys.path.insert(0, '../../../python')
import mxnet as mx
import numpy as np
import subprocess
import os
import time
import logging
import multiprocessing

logging.getLogger().setLevel(logging.DEBUG)

import ImageClassificationParams as params

# -- for imagenet validation -- #
# -- for cifar10 validation -- # 
val_data_dir = '/work/ImageNet-Tiny/data_sets/val'
val_csv_path = '/home/sainbar/work/ImageNet-Tiny/caffe/test_lmdb/test.csv'
#val_data_dir = '/work/datasets/cifar10/train'
#val_data_dir = 'F:/datasets/cifar10/train'
#val_csv_path = '/home/sainbar/work/caffe/cifar10/val.csv'

gpus = [2]
num_epoch
