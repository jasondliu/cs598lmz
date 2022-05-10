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

%matplotlib inline

# Global variables

# Simulation parameters

# Number of steps
n_steps = 100

# Number of agents
n_agents = 100

# Number of landmarks
n_landmarks = 10

# Number of dimensions
n_dim = 2

# Number of landmarks
n_landmarks = 10

# Number of dimensions
n_dim = 2

# Size of the world
world_size = 10.0

# Number of dimensions
n_dim = 2

# Size of the world
world_size = 10.0

# Number of
