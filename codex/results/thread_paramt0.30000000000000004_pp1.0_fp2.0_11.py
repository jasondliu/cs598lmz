import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
from matplotlib.widgets import Slider

# Import local modules
from lib.envs.simple_rooms import SimpleRoomsEnv
from lib.simulation import Experiment
from lib.envs.windy_gridworld import WindyGridworldEnv
from lib import plotting

# For plotting
%matplotlib inline

# Create environment
env = SimpleRoomsEnv()
# env = WindyGridworldEnv()

# Create value function
def create_value_function(env):
    """
    Creates value function for a given environment.
    """
    V = np.zeros(env.nS)
    return V

# Create policy
def create_random_policy(env):
    """
    Creates random policy for a given environment.
    """

