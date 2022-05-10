import gc, weakref
from collections import defaultdict

from . import utils
from . import events
from . import _compat
from . import _logging

log = _logging.get_logger(__name__)

_ROOT_NODE = None
_NODE_COUNT = 0
_NODE_CACHE = weakref.WeakValueDictionary()


class Node(object):
    """
    A node in the dependency graph.

    :param name: The name of the node.
    :param deps: A list of :class:`Node` objects this node depends on.
    :param func: A function that takes no arguments and returns the value of
        this node.
    :param func_kwargs: A dict of keyword arguments to pass to the function.
    :param volatile: If True, the value of this node will be recalculated
        every time it is requested.
    :param cache: If True, the value of this node will be cached.
    :param cache_type: If "timestamp", the value of this node will be cached
        until the timestamp of any of its dependencies
