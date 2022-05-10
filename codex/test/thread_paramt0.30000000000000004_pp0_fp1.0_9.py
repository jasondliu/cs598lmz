import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Normal

from IPython.display import clear_output
from matplotlib import animation
from IPython.display import display

import gym
from gym.wrappers import Monitor

import pybullet_envs
from pybullet_envs.bullet.kukaGymEnv import KukaGymEnv

import time

import os
import shutil

import imageio

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--env', type=str, default='KukaBulletEnv-v0')
parser.add_argument('--render', action='store_true')
parser.add_argument('--lr', type=float, default=0.001)
