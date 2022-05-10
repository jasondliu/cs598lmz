import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

# Create a figure with a subplot
fig = plt.figure()
ax = fig.add_subplot(111)

# Create a list of images to show
images = []

# Create a list of images to show
images = []

# Create a list of images to show
images = []

# Create a list of images to show
images = []

# Create a list of images to show
images = []

# Create a list of images to show
images = []

# Create a list of images to show
images = []

# Create a list of images to show
images = []

# Create a list of images to show
images = []

# Create a list of images to show
