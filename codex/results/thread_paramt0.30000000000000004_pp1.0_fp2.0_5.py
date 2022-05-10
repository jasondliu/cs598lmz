import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H"),daemon=True).start()

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
from matplotlib.widgets import Slider
from matplotlib.widgets import TextBox
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import CheckButtons

# Import modules
import constants
import functions
import classes

# Set up figure
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

# Set up axes
ax.set_xlim([0,constants.width])
ax.set_ylim([0,constants.height])
ax.set_aspect('equal')

# Set up buttons
ax_button_reset = plt.axes([0.8,0.9,0.1,0.05])
button_reset = Button(ax_button_
