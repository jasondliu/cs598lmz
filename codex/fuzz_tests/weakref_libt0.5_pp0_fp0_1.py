import weakref
import gc

import numpy as np

from . import util
from . import constants


class _BaseDict(object):
    """
    Base class for dictionaries.
    """

    def __init__(self, data=None, dtype=None):
        if data is None:
            data = {}
        elif not isinstance(data, dict):
            raise TypeError('data must be a dict')

        self._data = data
        self._dtype = dtype

    def __repr__(self):
        return '<%s(%r)>' % (self.__class__.__name__, self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._
