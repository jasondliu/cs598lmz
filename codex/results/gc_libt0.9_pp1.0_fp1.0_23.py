import gc, weakref, math
from numpy import nan, isnan, ndarray
from types import GeneratorType
from collections import defaultdict

__all__ = [
    'FrozenMapping',
    'FrozenOrderedDict',

    'TrivialFrozenOrderedDict',
    'TrivialFrozenMapping',

    'QuickWeakKeyCache',
    'MultiCache'
]


class FrozenOrderedDict(dict):
    """ Based on Raymond Hettinger's immutable OrderedDict implementation:
    http://code.activestate.com/recipes/576688-ordered-dictionary/
    But made immutable and added iterators (values, keys, ...)

    A variant of dict that remembers the order entries were added.
    >>> d = FrozenOrderedDict(a=1, b=2, c=3)
    >>> d['a']
    1
    >>> d.values()
    [1, 2, 3]
    >>> list(d.keys())
    ['a', 'b', 'd']
    """

    def __init__(self, *
