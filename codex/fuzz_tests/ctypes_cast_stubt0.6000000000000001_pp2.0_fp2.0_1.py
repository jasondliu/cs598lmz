import ctypes
ctypes.cast(0, ctypes.py_object).value

import numpy as np
import pandas as pd
import os
import time
import traceback
import datetime
import sys

from tqdm import tqdm
from collections import defaultdict
from IPython.display import clear_output

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

import gym
import gym.spaces
from gym.utils import seeding

from gym.envs.registration import register
register(
    id='FrozenLakeNotSlippery-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': False},
    max_episode_steps=100,
    reward_
