import threading
threading.stack_size(2000000000)

import array
import os
import sys

from math import sqrt, atan2, cos, sin

import numpy
import numpy.linalg

from pyflann import *
from pyflann.io.array_io import save_array, load_array
from pyflann.io.dataset_io import save_dataset, load_dataset
from pyflann.exceptions import FLANNException

from sklearn.cluster import MiniBatchKMeans

from scipy.cluster.vq import kmeans2

import time

from settings import *

from pointcloud import *

from pointprocessor import *

from utils import *

class Database:

	def __init__(self, file, n_clusters=50, max_features=20000, max_points=20000, max_neighbors=100, min_neighbors=1, max_error=0.1, index_method="kdtree", force_build=False, create_files=False):

