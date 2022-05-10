import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

from math import pi, sin, cos, sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def plot_3d_function(f, x_range, y_range, z_range, num_steps=10):
    x = np.linspace(*x_range, num_steps)
    y = np.linspace(*y_range, num_steps)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
   
