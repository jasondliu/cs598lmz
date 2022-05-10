import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#set up initial conditions

#set up grid
N = 100
x = np.linspace(0,1,N)
y = np.linspace(0,1,N)
X,Y = np.meshgrid(x,y)

#set up initial conditions
u = np.zeros((N,N))
v = np.zeros((N,N))

#set up diffusion coefficients
D_u = 0.1
D_v = 0.05

#set up reaction coefficients
a = 1
b = 0.5

#set up timestep
dt = 0.1

#set up plotting
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 1), ylim=(0, 1))
ax.grid()

