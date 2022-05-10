import mmap
from array import array
import sys
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from matplotlib import colors
from matplotlib.colors import LogNorm
import os
import matplotlib.colors as colors
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy import stats
import numpy as np
from numpy import linalg as LA

def routine_find_neighbors(x,y,z,dist_min,dist_max,Lx,Ly,Lz):
    neighbors = []
    for x_vec in range(-1,2):
        for y_vec in range(-1,2):
            for z_vec in range(-1,2):
                x_tmp = x + x_vec
                y_tmp = y + y_vec
                z_tmp = z + z_vec
                if x_tmp <
