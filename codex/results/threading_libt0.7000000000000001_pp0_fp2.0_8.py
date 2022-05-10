import threading
threading.stack_size(2**27)

import multiprocessing

from deap import creator, base, tools, algorithms

from math import sqrt
from random import randint, random, sample
from operator import attrgetter

from time import time
from functools import reduce
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
import psutil
import os

#from utils import *
from problem_1 import Problem
from preprocessing import *
from sklearn.datasets import make_blobs
def initial_population():
	clusters = []
	for _ in range(n_clusters):
		cluster = make_blobs(n_samples=n_points, n_features=n_dimensions, centers=1,
			cluster_std=0.3, center_box=(-4.0, 4.0), shuffle=False, random_state=None)[0]
		clusters.append(cluster)
	return np.vstack(clusters)

def eval_function(individual
