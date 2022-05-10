import sys, threading
threading.Thread(target=lambda: time.sleep(10*60)).start()

import os, json, random, shutil, pickle, math, re, cProfile
sys.path.append("..")
import numpy as np
import tensorflow as tf
from tqdm import tqdm
from time import time
from collections import Counter
from utils.data_utils import *
from utils.utils import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors

os.environ['CUDA_VISIBLE_DEVICES'] = '1'

PATH = '../data/'
TRAIN_PATH = PATH + 'train/'
TEST_PATH = PATH + 'test/'

TRAIN_IMG_PATH = TRAIN_PATH + 'images/'
TRAIN_JSON_PATH = TRAIN_PATH + 'via_region_data.json'
TEST_IMG_PATH = TEST
