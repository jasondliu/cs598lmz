import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle

from scipy.spatial.distance import pdist, squareform

import time

# Define parameters

# Number of particles
N = 50

# System size
L = 1.0

# Particle radius
R = L/2.0/N

# Particle mass
m = 1

# Time step
dt = 1e-2

# Number of time steps
nsteps = 100000

# Particle positions
x = np.random.uniform(0, L, N)
y = np.random.uniform(0, L, N)

# Particle velocities
vx = np.zeros(N)
vy = np.zeros(N)

# Particle forces
fx = np.zeros(N)
fy = np.zeros(N)

# Part
