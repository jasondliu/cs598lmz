import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from IPython.display import HTML

from matplotlib import rc
rc('animation', html='html5')

