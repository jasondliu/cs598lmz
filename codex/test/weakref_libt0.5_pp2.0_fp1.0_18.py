import weakref

import numpy as np

from .utils import _is_writable, _is_writable_array

__all__ = ['CachedArray', 'CachedArrayMixin', 'CachedArrayMeta']


class CachedArray(object):
    """A wrapper to cache the value of a NumPy array.

    This class can be used to cache the value of a NumPy array. The
    wrapped array can be accessed via the `array` attribute and the
    cached value can be accessed via the `value` attribute. When the
    wrapped array is modified, the cached value is invalidated and
    recomputed when it is next accessed.

    The wrapped array must be writable.

    Parameters
    ----------
    array : array_like
        The array to wrap.
    value : array_like, optional
        The cached value, by default None.
    """
    def __init__(self, array, value=None):
        if not _is_writable_array(array):
            raise ValueError('array must be writable')
        self._array = array
