import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import time

def get_data():
    data = np.random.rand(10, 10)
    return data

fig = plt.figure()

data = get_data()
im = plt.imshow(data, interpolation='none', animated=True)

def updatefig(*args):
    global data
    data = get_data()
    im.set_array(data)
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=100, blit=True)
plt.show()
