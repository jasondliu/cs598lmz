import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# Import the necessary modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use('seaborn-pastel')

# Set the number of frames
nframes = 100

# Set the number of atoms
natoms = 100

# Set the box size
box_size = np.array([100.0, 100.0])

# Set the initial atom positions
x = np.random.uniform(0.0, box_size[0], natoms)
y = np.random.uniform(0.0, box_size[1], natoms)

# Set the initial atom velocities
vx = np.random.normal(0.0, 1.0, natoms)
vy = np.random.normal(0.0, 1.0, natoms)

# Set the atom masses
m = np.ones(natoms)

# Set the tim
