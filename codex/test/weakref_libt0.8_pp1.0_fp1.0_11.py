import weakref
from . import Environment, MDPInfo
from . import spaces
from .utils.random import np_random
from .utils import logger

#TODO:
#self._env.monitor should be self._env.env.monitor
class VecEnv(object):
    """
    An abstract asynchronous, vectorized environment.
    """
    closed = False
    viewer = None
    metadata = {'render.modes': []}
    reward_range = (-float('inf'), float('inf'))
    spec = None

    def step_async(self, actions):
        """Tell all the environments to start taking a step
        with the given actions.
        Call step_wait() to get the results of the step.
        You should not call this if a step_async run is
        already pending.
        """
        pass

