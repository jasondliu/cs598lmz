import weakref
from collections.abc import Mapping
import types
import operator

from .compat import collection_abc
from .compat import collections_abc
from .compat import builtins
from .compat import py_v

from . import weak_dict
from . import weak_set

import logging
logger = logging.getLogger(__name__)

class WeakValDict(weak_dict.WeakDict):

    def __init__(self, data=None, weak_set=weak_set.WeakSet):
        super().__init__()
        self._weak_set = weak_set
        if data:
            self.update(data)

    def __getitem__(self, key):
        return self._weak_set(super().__getitem__(key))

    def __setitem__(self, key, value):
        if isinstance(value, weak_set.WeakSet):
            weak_set = value
        else:
            weak_set = self._weak_set(value)
        super().__setitem__(key, weak_set)


