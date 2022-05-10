import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

import numpy as np
import gym
import gym_microrts
import time

from stable_baselines import PPO2
from stable_baselines.common.policies import CnnPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines.common.callbacks import CheckpointCallback
from stable_baselines.common.callbacks import EvalCallback
from stable_baselines.results_plotter import load_results, ts2xy
from stable_baselines.bench import Monitor

from microrts.rts_wrapper.env_wrapper import *
from microrts.settings import *
from microrts.rts_wrapper.utils import *

import os
import datetime
import random

random.seed(1)
np.random.seed(1)

# Create log dir
log_dir = "./tmp/gy
