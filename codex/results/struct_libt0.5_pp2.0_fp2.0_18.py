import _struct

# include the directory of this file
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# include common packages
from common import *

# include vrep 
import vrep

# include the path of pybrain
# sys.path.append('C:/Users/julius/Desktop/pybrain')
sys.path.append('C:/Users/julius/Desktop/pybrain')

# include pybrain
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q, SARSA
from pybrain.rl.experiments import Experiment
from pybrain.rl.environments import Task

# include the path of pygame
sys.path.append('C:/Python27/Lib/site-packages/pygame')

# include pygame
import pygame

# include numpy
import numpy as np

# include matplotlib
import matplotlib.pyplot as plt

# create
