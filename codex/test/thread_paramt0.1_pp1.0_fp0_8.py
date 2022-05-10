import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.integrate import odeint
from scipy.optimize import minimize

from sklearn.metrics import mean_squared_error

from IPython.display import HTML

#%matplotlib inline

#plt.rcParams['animation.html'] = 'html5'

#plt.rcParams['figure.figsize'] = [10, 5]

#plt.rcParams['animation.writer'] = 'avconv'

#plt.rcParams['animation.codec'] = 'h264'

#plt.rcParams['font.size'] = 16

#plt.rcParams['axes.labelsize'] = 16

#plt.rcParams['xtick.labelsize'] = 12

#plt.rcParams['ytick.labelsize'] = 12

