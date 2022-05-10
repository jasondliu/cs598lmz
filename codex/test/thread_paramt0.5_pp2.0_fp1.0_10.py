import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

#%%

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#%%

#Number of points
N = 100

#Time step
dt = 0.01

#Number of time steps
n = 10000

#Initial conditions
x = np.linspace(0,1,N)
y = np.linspace(0,1,N)

#Initial function
u0 = np.zeros((N,N))
u0[0,:] = np.sin(2*np.pi*x)
u0[:,0] = np.sin(2*np.pi*y)
