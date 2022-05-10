import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import time

import random

import math

import cv2

import os

import copy

import pickle

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

import torchvision.transforms as T

import gym
from gym.envs.registration import register

import ppaquette_gym_doom
from ppaquette_gym_doom.wrappers.action_space import ToDiscrete

import skimage.color, skimage.transform

import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import matplotlib.pyplot as plt
import
