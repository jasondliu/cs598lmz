import weakref

import numpy as np

from . import utils
from . import core
from . import _core
from . import array
from .array import Array
from . import ufunc
from . import _ufunc
from . import types


def _copy_to_list(dest, src, length):
    for i in range(length):
        dest[i] = src[i]


class ArrayType(type):
    """Metaclass for Array

    This is used to register all Array subclasses created, and to
    cache them by their shape, so that multiple instances of an array
    with the same shape can share the same class.
    """

    _cache = {}

    @classmethod
    def _clear_cache(cls):
        cls._cache.clear()

    def __new__(cls, name, bases, attrs):
        new_class = super(ArrayType, cls).__new__(cls, name, bases, attrs)

