import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

# Set up some global variables for the plotting
# Plotting Stuff
FPS = 60
dt = 1 / FPS
plot_duration = 15
running_plot_duration = plot_duration
sample_duration_ms = int(dt * 1000)

# Import necessary libraries
import math, sys
import numpy as np
import torch
from torch.autograd import Variable
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from matplotlib.animation import FuncAnimation

# Import local libraries
sys.path.append('../../')
from networks.networks import PandaAE
from dataset.datasets import PandaDataset

# Import mpl_toolkits.mplot3d for 3D plotting
from mpl_toolkits.mplot3d import axes3d, Axes3D

