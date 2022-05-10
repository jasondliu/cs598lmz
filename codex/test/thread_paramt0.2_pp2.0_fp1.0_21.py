import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import minimize

import time

import os
import sys

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

from torch.utils.data import Dataset, DataLoader

from torchvision import transforms, utils

from sklearn.preprocessing import MinMaxScaler

import pandas as pd

import copy

import pickle

from scipy.stats import norm

from scipy.stats import multivariate_normal

from scipy.stats import invwishart

from scipy.stats import wishart

from scipy.stats import gamma

from scipy.stats import dirichlet

