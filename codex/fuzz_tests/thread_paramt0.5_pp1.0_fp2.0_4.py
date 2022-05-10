import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#%%
# Define the function
def f(x, y):
    #return (1.0 - x / 2.0 + x**5 + y**3) * np.exp(-x**2 -y**2)
    return np.exp(-(x**2 + y**2))


#%%
# Define the grid
N = 100
x = np.linspace(-4, 4, N)
y = np.linspace(-4, 4, N)
X, Y = np.meshgrid(x, y)


#%%
# Plot the surface
fig = plt.figure()
ax = fig.gca(projection='3d')
