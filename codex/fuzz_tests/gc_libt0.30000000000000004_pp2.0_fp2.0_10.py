import gc, weakref
import logging

from . import _compat
from . import _util
from . import _weakref

log = logging.getLogger(__name__)

#=============================================================================
# weakrefs
#=============================================================================

class _WeakRef(object):
    """
    A weakref that can be used as a key in a dict.
    """
    __slots__ = ('_obj', '_key')

    def __init__(self, obj):
        self._obj = weakref.ref(obj)
        self._key = id(obj)

    def __call__(self):
        return self._obj()

    def __hash__(self):
        return self._key

    def __eq__(self, other):
        return self._key == other._key

    def __ne__(self, other):
        return self._key != other._key

class _WeakKeyDictionary(dict):
    """
    A dictionary that uses weak references for its keys.
    """
    def __init__(self, *args, **kwargs):
        super
