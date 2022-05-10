import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection

from scipy.integrate import odeint

from numpy.random import randn
from numpy.random import rand
from numpy.random import uniform

from math import sin
from math import cos
from math import pi
from math import sqrt
from math import atan2
from math import floor

from time import sleep

# Global variables

# Simulation parameters
dt = 0.001
t_max = 10
t = np.arange(0, t_max, dt)

# World parameters
world_size = 20

# Robot parameters
robot_size = 0.5
robot_speed = 1

# Goal parameters
goal_size = 0.5

# Obstacle parameters
obstacle_size = 1

# Sensor parameters
