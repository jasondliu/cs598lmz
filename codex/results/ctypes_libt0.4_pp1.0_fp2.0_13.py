import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time

# This is a simple example of a matplotlib animation
#
# The main things to note are:
#
#  * The call to animation.FuncAnimation, which specifies the figure to animate,
#    the function that is called at each frame, and the interval between frames.
#  * The call to time.sleep in the function that is called at each frame.  This
#    is what limits the speed of the animation.
#

fig = plt.figure()
ax = fig.add_subplot(111)

# Initialize the data
x = np.arange(10)
y = np.zeros(10)

# Initialize the line that will be updated
line, = ax.plot(x, y, 'r-')

# This function will be called at each frame
def update(data):
    line.set_ydata(data)
    return line,
