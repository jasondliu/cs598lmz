import types
types.SimpleNamespace()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle
import shutil

from scipy.ndimage.filters import gaussian_filter

import torch
import torch.nn.functional as F
import torch.optim as optim
import torch.nn as nn

import os
import cv2
import sys
import copy
import math
import time

# from data.utils import *

from model.pointnet import *

import glob

# from data.download_datasets import ModelNet40
# from data.download_datasets import ShapeNet

# import open3d as o3d

def main():
    # ---------
    # parse args
    args = argparse.ArgumentParser()
    args.add_argument('--exp', type=str, default='exp_chair')
    args.add_argument('--dataset', type=str, default='mn40')
    args.add_argument('--batch_size
