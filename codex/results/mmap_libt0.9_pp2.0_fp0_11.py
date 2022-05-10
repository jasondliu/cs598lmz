import mmap

import os
# os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
# os.environ["CUDA_VISIBLE_DEVICES"]="2"

import cv2
import numpy as np
import sys

if sys.version_info[0] == 2:
    import cPickle as pkl
else:
    import pickle as pkl
import math as m
from random import randint


class ScreenDetector(object):

    def __init__(self, classifier_path='./screen_classifier',use_cuda=True):
        self.use_cuda = use_cuda

        with open(os.path.join(classifier_path, 'model_cache/screenIdx_t10.dic'), 'rb') as f:
            self.c_idx = pkl.load(f)

        if self.use_cuda:
            self.cuda_screen_detector = ScreenDetectorCuda(model_path=os.path.join(classifier_path, 'model
