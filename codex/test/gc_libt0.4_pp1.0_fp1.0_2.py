import gc, weakref
from collections import defaultdict
import sys

#------------------------------------------------------------------------------
# Python 2/3 compatibility
#------------------------------------------------------------------------------

if sys.version_info[0] == 2:
    from itertools import izip as zip

#------------------------------------------------------------------------------
# Weak reference utilities
#------------------------------------------------------------------------------

class WeakMethod(object):
    """
    A weak reference to a method.
    """

    def __init__(self, func):
        """
        Create a weak reference to a method.
        """
        self.__func = func.im_func
        self.__self = weakref.ref(func.im_self)

    def __call__(self, *args, **kwargs):
        """
        Call the method.
        """
        return self.__func(self.__self(), *args, **kwargs)

#------------------------------------------------------------------------------
# Signal/slot system
#------------------------------------------------------------------------------

class Signal(object):
    """
    A signal/slot system.
    """

    def __init__(self):
        """
        Create a new signal.
        """
