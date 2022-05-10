import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import numpy as np
import time

def plot_grid(grid, ax=None, cmap='gray'):
    if ax is None:
        ax = plt.gca()
    ax.set_aspect('equal')
    ax.set_xticks(np.arange(grid.shape[1]) - 0.5)
    ax.set_yticks(np.arange(grid.shape[0]) - 0.5)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(which='major', color='k', linestyle='-', linewidth=2)
    ax.set_xlim(-0.5, grid.shape[1] - 0.5)
    ax.set_ylim(-0.5, grid.shape[0
