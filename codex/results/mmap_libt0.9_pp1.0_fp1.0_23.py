import mmap
import numpy as np
import time

# User Inputs
xsize = 5.0
ysize = 5.0
nx = 200
ny = 400

alpha = 1.8e-3
T0 = 200
Ts = 100

tEnd = 2000
timestep = 0.01

# Calculate the delta x and deltay
dx = xsize/nx
dy = ysize/ny

# Calculate Intermediate Values
dx2 = dx*dx
dy2 = dy*dy

nxm1 = nx-1
nym1 = ny-1

# Initialize Data Structure
# Next - Contains data for current timestep
# Last - Contains data for the previous timestep
next = np.matrix.transpose(np.tile(T0, (ny, nx)))
last = np.matrix.transpose(np.tile(T0, (ny, nx)))

# Write Data to Disk as Binary
with open('next{0}x{1}_{2}.dat'.format(nx,ny,tEnd),"wb")
