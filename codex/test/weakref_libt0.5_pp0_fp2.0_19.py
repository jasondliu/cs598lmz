import weakref

from . import log
from . import util


class State(object):
    """
    State of a single object.
    """

    def __init__(self, obj):
        self._obj = weakref.ref(obj)
        self.dirty = False
        self.dirty_children = False
        self.dirty_parents = False
        self.dirty_siblings = False

    def __str__(self):
        return 'State(%s, %s)' % (self._obj(), str(self.__dict__))


class StateEngine(object):
    """
    Engine to track the state of a tree of objects.
    """

    def __init__(self):
        self._state_map = {}

    def get_state(self, obj):
        """
        Get the state of the given object.
        """
        state = self._state_map.get(obj)
