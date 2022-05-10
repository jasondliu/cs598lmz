import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

from scipy.integrate import odeint
from scipy.optimize import minimize

from IPython.display import HTML

from matplotlib import rc
rc('animation', html='html5')

