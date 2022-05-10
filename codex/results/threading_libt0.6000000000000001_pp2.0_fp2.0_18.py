import threading
threading.stack_size(67108864)

import sys
sys.path.append("game/")
import wrapped_flappy_bird as game
game_state = game.GameState()

try:
    from dqn_agent import DQNAgent
except Exception as e:
    raise ImportError("Can not import DQN Agent")

from pygame.constants import K_w
from pygame.constants import K_s

import random

ACTIONS = 2  # possible actions: jump, do nothing
GAMMA = 0.99  # decay rate of past observations
OBSERVE = 100000.  # timesteps to observe before training
EXPLORE = 2000000.  # frames over which to anneal epsilon
FINAL_EPSILON = 0.0001  # final value of epsilon
INITIAL_EPSILON = 0.0001  # starting value of epsilon
REPLAY_MEMORY = 50000  # number of previous transitions to remember
BATCH = 32  # size of minibatch
FRAME_PER_ACTION =
