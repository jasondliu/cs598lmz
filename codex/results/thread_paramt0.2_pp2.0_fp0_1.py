import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.integrate import odeint
from scipy.optimize import minimize

from sklearn.metrics import mean_squared_error

from IPython.display import clear_output

import time

#%matplotlib inline

#%config InlineBackend.figure_format = 'retina'

#plt.rcParams['figure.figsize'] = [12, 4]

#plt.rcParams['animation.html'] = 'html5'

#plt.rcParams['animation.writer'] = 'ffmpeg'

#plt.rcParams['animation.codec'] = 'h264'

#plt.rcParams['animation.bitrate'] = -1

#plt.rcParams['animation.embed_limit'] = 200


