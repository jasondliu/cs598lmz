from bz2 import BZ2Decompressor
BZ2Decompressor

# Load the model content from disk
mm_mdl = mx.model.load_checkpoint(prefix=prefix, iteration=iteration)
# end

# Imports
from __future__ import print_function
import mxnet as mx
from mxnet import nd, autograd, gluon
import numpy as np
import os, sys
import tarfile
import platform
import urllib.request
import tarfile
import cv2

# hyper parameters
ctx = mx.cpu()
num_classes = 000 # set it in data_loader
dataset_name = 'Kaggle_Plant_Seedlings'
batch_size = 1
lr = 0.0001
epochs = 15
classes = [0, 1, 2]
rotation_angle = 20 # degrees

# image info
w = 100
h = 100
c = 3

# mean std 
mean = np.array([0.485, 0.456, 0.406])
std = np.array([0.229, 0.224, 0.225])

# for
