import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

########################################################################################################################

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

########################################################################################################################

def init_plot(ax, lim_x, lim_y, lim_z, grid_x, grid_y, grid_z):
    ax.set_xlim(lim_x)
    ax.set_ylim(lim_y)
    ax.set_zlim(lim_z)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.grid(grid_x, grid_y, grid_z)

def init_plot_2d(ax, lim_x, lim_y, grid_x, grid_y):
    ax.set_xlim(lim_x
