import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import fsolve

from matplotlib import rc
import matplotlib as mpl
rc('font',**{'family':'serif','serif':['Times'],'size':10})
rc('text', usetex=True)

import time

