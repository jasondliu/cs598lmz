import signal
signal.signal(signal.SIGINT, signal_handler)

import sys
import time

from ops import *
import utils.logger as logger

#1. define a class for our model
class CycleGAN(object):
    def __init__(self,
                 sess,
                 epoch,
                 batch_size,
                 dataset_name,
                 checkpoint_dir,
                 result_dir,
                 log_dir,
                 image_size,
                 sample_size,
                 output_size,
                 input_c_dim,
                 output_c_dim,
                 L1_lambda=10,
                 use_resnet=True,
                 use_lsgan=True,
                 norm='instance',
                 learning_rate=2e-4,
                 beta1=0.5,
                 ngf=64
                 ):
        """
        Args:
            sess : TensorFlow session
            batch_size : The size of batch. Should be specified before training.
            image_size : Image size.
            output_size : (optional) The resolution in pixels
