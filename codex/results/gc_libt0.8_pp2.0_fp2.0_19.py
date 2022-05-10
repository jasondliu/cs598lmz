import gc, weakref
import inspect

from ltk.operate import operate
from ltk.actions import Actions
from ltk.pickle_util import PickleUtil
from ltk.logger import Logger

from ltk.constants import Constants
constants = Constants()

class Controller(object):
    def __init__(self, actions=None, logger=None):
        if actions is None:
            self.actions = Actions()
        else:
            self.actions = actions
        self.logger = Logger(logger)
        self.operate = operate
        self.pickle_util = PickleUtil(self.actions, self.logger)
        self._add_actions()

    def __del__(self):
        # del self.actions
        # del self.pickle_util
        # del self.logger
        # del self.operate
        # gc.collect()
        pass

    def _add_actions(self):
        actions = inspect.getmembers(self.actions, predicate=inspect.ismethod)
        for (name
