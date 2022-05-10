import gc, weakref, inspect
from collections import deque
from itertools import chain
from functools import wraps
from math import ceil
from hashlib import sha256
from os import urandom
from types import BuiltinMethodType

from . import utils as _utils
from . import api as _api
from . import exceptions as _exc
from . import internals as _internals
from . import weakrefs as _weakrefs


class _Meta(type):
    """Metaclass for the ``_Proxy`` class."""
    def __new__(mcls, name, bases, clsdict):
        # Ensure that proxy types are always immutable
        clsdict.update({
            '__slots__': (),
            '__hash__': None,
            '__new__': None,
            '__init__': None,
            '__del__': None,
            '__setattr__': None,
            '__delattr__': None,
            '__dir__': None,
            '__repr__': None,
            '__getattribute__': None,
            '
