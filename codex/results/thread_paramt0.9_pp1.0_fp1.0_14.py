import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()
from copy import copy

import numpy as np
import torch
from IPython import display
from tqdm import tqdm

import time

import sys
from models import *
from utils import *
from test import *




env_name = sys.argv[1]    
sr_method = "minimum_distance"    
sr_method = sys.argv[2]

if len(sys.argv)>3 and "ablation" in sys.argv[3]:
    sr_method = "ablation"



env = gym.make(env_name)


print(env_name)
render = False


# Configs
verbose = False
visited_map = None
converge_thresh = .95
iterations = 10000

n = env.n
m = env.m
c = env.c
t = env.t


initial_height_map = np.array(
    [[1, 1, 1],

