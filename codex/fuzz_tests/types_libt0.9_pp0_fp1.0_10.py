import types
types.ModuleType.__getitem__ = lambda self, key: getattr(self, key)
import GraphTool
import random
random.seed(2017)

# set up matplotlib
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pylab as pylab
pylab.rcParams['figure.figsize'] = 16.0, 12.0

import matplotlib.pyplot as plt

import GraphTool.all as gt

# %matplotlib inline

import graph_tool.all as gt
import graph_tool
import numpy as np
import pandas as pd

from multiprocessing import Process, Queue

import networkx as nx
import glob
import os
import datetime
import uuid

import powerlaw
import random
random.seed(2017)
np.random.seed(2017)

import scipy.stats

from riotwatcher import RiotWatcher
from game import Game
sys.path.insert(0, '..')
from src.load_data import open_
