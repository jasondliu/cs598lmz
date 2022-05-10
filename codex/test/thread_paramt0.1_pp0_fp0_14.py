import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import minimize

from IPython.display import HTML

from matplotlib import rc
rc('animation', html='html5')

from matplotlib import rcParams
rcParams['figure.figsize'] = (10, 6)
rcParams['font.size'] = 16
rcParams['animation.embed_limit'] = 2**128

from matplotlib import animation, rc
from IPython.display import HTML

from matplotlib import rcParams
rcParams['figure.figsize'] = (10, 6)
rcParams['font.size'] = 16
rcParams['animation.embed_limit'] = 2**128

from matplotlib import animation, rc
from IPython.display import HTML

from matplotlib import rcParams
