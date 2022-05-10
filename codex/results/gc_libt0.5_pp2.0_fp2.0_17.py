import gc, weakref
from collections import defaultdict
from functools import partial
from itertools import chain
from operator import itemgetter
from types import MethodType

from six import add_metaclass, itervalues

from .util import get_weakref_proxy
from . import util


# XXX: We want to avoid using the same names as the attributes of the
#      objects we are wrapping.  Maybe we should use a different prefix?
_DICT_ATTR_PREFIX = '_dict_'
_DICT_ATTR_PREFIX_LEN = len(_DICT_ATTR_PREFIX)


class _DictLike(object):
    """
    A base class for dict-like objects.

    This class is not intended to be used directly.

    Subclasses must override __getitem__ and __setitem__.
    """

    def __init__(self, dict_=None):
        if dict_ is None:
            dict_ = {}
        self._dict = dict_

    def __contains__(self, key):
        return key in self._dict
