import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
# Env

from gym import Env
from gym.spaces import Discrete, Box
from gym.utils import seeding

class FooEnv(Env):
    """
    The Foo Environment
    """

    def __init__(self):
        self.action_space = Discrete(2)
        self.observation_space = Box(low=0, high=1, shape=(1,))
        self.seed()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action)
        if action == 0:
            reward = 0
            done = False
            obs = 0
        elif action == 1:
            reward = 1
            done = True
            obs = 0
        return obs, reward, done, {}

    def reset(self):
        return 0


# ___________________________________________________________________________
# Wra
