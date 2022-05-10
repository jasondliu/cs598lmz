import weakref
from . import _compat
from . import _compat_pickle
from . import _compat_collections_abc
from . import _compat_collections
from . import _compat_functools
from . import _compat_pickle
from . import _compat_weakref


class LRUCache(object):
    """
    An implementation of a least-recently-used (LRU) cache. This cache
    has a fixed size specified in the constructor. If you try to put
    more items into the cache than it can hold, the least-recently-used
    item will be discarded.
    An item is considered to be used when it is retrieved, inserted,
    or updated.

    >>> lru = LRUCache(3)
    >>> lru['foo'] = 'bar'
    >>> lru['baz'] = 'qux'
    >>> len(lru)
    2
    >>> 'foo' in lru
    True
    >>> 'baz' in lru
    True
    >>> 'quux' in lru
    False
    >>>
