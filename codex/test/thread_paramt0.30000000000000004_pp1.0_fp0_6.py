import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#%%

def plot_animation(x, y, z, x_label, y_label, z_label, title, x_range, y_range, z_range, fps=30, save_as=None):
    fig = plt.figure()
    ax = plt.axes(xlim=x_range, ylim=y_range, zlim=z_range)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    ax.set_title(title)
    line, = ax.plot([], [], [], lw=2)
    
    def init():
        line.set_data([], [])
        line.set_3d_properties([])
        return line,
    
   
