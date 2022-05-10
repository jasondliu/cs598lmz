import weakref
# Test weakref.ref objects
from test import support
import re
import io
from random import randrange, shuffle
import abc
from collections import deque
import contextlib
import itertools


class ListTreePrinter(object):
    """Print a tree using a list of lists representation.

    Based on the list of lists tree printing contributed by Andrew Dalke
    to the comp.lang.python newsgroup, 23 Jan 2001. http://groups.google.com/
    group/comp.lang.python/msg/f401c424b08absiw
    """
    class _printer(object):
        def __init__(self, obj):
            self.obj = obj
            self.seen = set()

        def add(self, obj):
            if id(obj) not in self.seen:   # Avoid infinite loop, see issue6416
                self.seen.add(id(obj))
                if isinstance(obj, (list, tuple, set)):
                    self.stack.append(obj)

        def printer(self, obj):
            # The next lines shut up PyEval_GetRestricted,
