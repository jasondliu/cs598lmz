import threading
threading.stack_size(67108864)

sys.path.insert(0,'/home/raghunath/datasets/VQA/PythonHelperTools')
sys.path.insert(0,'/home/raghunath/datasets/VQA/PythonEvaluationTools')

import vqaTools
import vqaEvaluation

import os
import operator
import argparse

import pickle
import h5py
import json
import random
import numpy as np
import pandas as pd
import skimage.io as io

from collections import OrderedDict

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.autograd as autograd
from torch.autograd import Variable

from sklearn.metrics import accuracy_score

import timeit

def get_image_features(img_id,dataset,img_feats):
    index = dataset['data']['coco_id_to_index'][img_id]
    return
