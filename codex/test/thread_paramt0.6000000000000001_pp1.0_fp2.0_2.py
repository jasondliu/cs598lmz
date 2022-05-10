import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

from constants import *
import numpy as np
import time
import math
import random
import os
import logging

import torch
import torch.nn as nn
import torch.optim as optim

from agent import Agent
from memory import Memory
from utils import *

use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")

def train(env, agent, memory, batch_size=64, gamma=0.99, update_freq=4,
          target_update_freq=2000, num_episodes=1000, max_steps=1000,
          logging_freq=1, logdir=None):
    """
    Train a DQN agent with given parameters.
    """
    # Create log folder if it doesn't exist
    if logdir is not None and not os.path.exists(logdir):
        os.makedirs(logdir)

    # Set up logging
