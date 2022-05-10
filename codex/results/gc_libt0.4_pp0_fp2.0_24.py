import gc, weakref
from collections import defaultdict
from functools import wraps

from . import _py3k

__all__ = ['WeakKeyDictionary', 'WeakValueDictionary', 'WeakSet']

if _py3k:
    from collections import UserDict
    from weakref import WeakKeyDictionary as _WeakKeyDictionary
    from weakref import WeakValueDictionary as _WeakValueDictionary
    from weakref import WeakSet as _WeakSet
else:
    from UserDict import UserDict as _UserDict
    from _weakref import WeakKeyDictionary as _WeakKeyDictionary
    from _weakref import WeakValueDictionary as _WeakValueDictionary
    from _weakref import WeakSet as _WeakSet

def _remove_dead_weakref(d, key, wr):
    try:
        del d[key]
    except KeyError:
        pass

class WeakKeyDictionary(_WeakKeyDictionary):
    """A WeakKeyDictionary is a mutable mapping class that stores
    weak references to its keys.

    Entries in the dictionary will be discarded when there
