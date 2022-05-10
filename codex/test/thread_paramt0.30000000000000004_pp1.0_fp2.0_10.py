import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

import gym
from gym import spaces
from gym.utils import seeding

from gym_minigrid.minigrid import *
from gym_minigrid.register import register

class FourRooms(MiniGridEnv):
    """
    Four rooms grid environment, see
    https://arxiv.org/abs/1507.06527
    The agent starts in a random position in one of the four rooms and
    has to reach the goal in another room.
    """
