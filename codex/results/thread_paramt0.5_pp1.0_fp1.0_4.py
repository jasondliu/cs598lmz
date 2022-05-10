import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import colors
import numpy as np
import random

'''
    This is a cellular automaton that simulates the spread of fire on a forest
    that is represented by a 2D grid.
    The grid is populated with trees (represented by 1) and empty spaces (represented by 0).
    The trees can catch fire if they are adjacent to a tree that is burning.
    A tree that catches fire will burn for one turn, and then become an empty space.
    On each turn, a random tree catches fire.
'''

# Set the initial state of the grid
grid = np.zeros((100,100), dtype=int)
grid[50,:] = 1
grid[:,50] = 1

grid[10,10] = 2
grid[10,11] = 2
grid[10,12] = 2
grid[10,13] = 2
grid[10,
