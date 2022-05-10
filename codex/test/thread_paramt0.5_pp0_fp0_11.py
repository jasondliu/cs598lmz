import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import pylab as pl
import numpy as np
import matplotlib.image as mpimg
import random
import time
import math

# Parameters
n = 100
p = 0.3
q = 0.3

# Initialize grid
grid = np.zeros(shape=(n,n))

# Initialize cells
for i in range(n):
    for j in range(n):
        if random.random() < 0.5:
            grid[i][j] = 1

# Initialize figure
fig = pl.figure()
ax = fig.add_subplot(111)

# Plot initial grid
imgplot = pl.imshow(grid, interpolation='nearest')

# Run simulation
for iteration in range(50):

    # Update image
    imgplot.set_data(grid)
    fig.canvas.draw()

    # Copy grid
    newGrid = np.copy(grid)

    # Update cells
