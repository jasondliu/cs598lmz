import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

from PIL import Image
from io import BytesIO
from IPython.display import clear_output, Image, display

import gym
from gym import spaces
from gym.utils import seeding

from gym_minigrid.minigrid import *
from gym_minigrid.register import register

from gym_minigrid.wrappers import *

class MiniGridEnv(gym.Env):
    """
    Base class for all MiniGrid environments
    """

    metadata = {
        'render.modes': ['human', 'rgb_array']
    }

    def __init__(
        self,
        grid_size=16,
        max_steps=100,
        see_through_walls=False,
        agent_view_size=7
    ):
        self.grid_size = grid_size
        self.max_
