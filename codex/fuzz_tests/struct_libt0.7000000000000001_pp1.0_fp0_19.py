import _struct
import base64
import functools
import pkg_resources

import numpy as np

import gym
from gym import spaces
from gym.utils import seeding

try:
    import pybullet_envs
except ImportError:
    pass

try:
    import mujoco_py
except ImportError:
    pass

logger = logging.getLogger(__name__)


# ================================================================
# OpenAI Gym
# ================================================================

class Env(object):
    r"""The main OpenAI Gym class. It encapsulates an environment with
    arbitrary behind-the-scenes dynamics. An environment can be
    partially or fully observed.

    The main API methods that users of this class need to know are:

        step
        reset
        render
        close
        seed

    And set the following attributes:

        action_space: The Space object corresponding to valid actions
        observation_space: The Space object corresponding to valid observations
        reward_range: A tuple corresponding to the min and max possible rewards

    The methods are accessed publicly as "step", "reset", etc
