import ctypes
ctypes.cdll.LoadLibrary("/usr/lib/libboost_python.so")
import os.path as osp
from shutil import copyfile
import numpy as np
from torch import nn as nn
from torch.nn import functional as F
import torch
import os
import pickle
from util import *
import math
import argparse
from collections import deque
import sys
from threading import Thread
from multiprocessing import cpu_count
from copy import copy
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


class PPO():
    def __init__(self, render, load_model, model_path, eval_mode, save_path,
                 action_dim, state_dim, high, low, stack_size, total_episodes,
                 render_freq, save_freq, test_step, trade_step, delay_step, penalty,
                 max_step, gamma, lam, K, sample_batch_size, train_batch_size,
                 actor_lr, critic_lr):
        """
