import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start() # to flush stdout

import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.spatial import distance
import time

import os
import sys
import cv2
import numpy as np
import math
import time
import argparse
from utils import *
from darknet import Darknet
from preprocess import prep_image, inp_to_image
import pandas as pd
import random
import pickle as pkl
import itertools

def get_test_input(input_dim, CUDA):
    img = cv2.imread("dog-cycle-car.png")
    img = cv2.resize(img, (input_dim, input_dim)) 
    img_ =  img[:,:,::-1].transpose((2,0,1))
    img_ = img_[np.newaxis,:,:,:]/255.0
    img_ = torch.from_numpy(img_).float()
    img_ =
