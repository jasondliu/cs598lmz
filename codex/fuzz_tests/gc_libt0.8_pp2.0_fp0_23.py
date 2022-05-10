import gc, weakref
from weakref import WeakValueDictionary
import types
from warnings import warn
from collections import deque
from collections import defaultdict
from collections import namedtuple
from collections import OrderedDict
from collections import Iterable
from typing import Callable
import abc


if sys.version_info < (3, 6):

    class abc(object):

        __metaclass__ = types.ABCMeta

        class abstractmethod(abc.abstractmethod):

            def __init__(self, funcobj):
                try:
                    funcobj.__isabstractmethod__ = True
                except (TypeError, AttributeError):
                    pass


else:

    abc = abc
    abc.abstractmethod = abc.abstractmethod


abc.abstractmethod.__module__ = "abc"
abc.abstractmethod.__qualname__ = "abstractmethod"

if sys.version_info < (3, 7):

    def iscoroutinefunction(func: object) -> bool:
        """Return True if func is a coroutine function, False if not."""

