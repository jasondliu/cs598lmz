import weakref

import numpy as np

from .lambdop import Lambdop


def _normalize_shape(shape):
    """
    Ensures a proper shape tuple.
    """
    if isinstance(shape, int):
        shape = (shape,)
    return tuple(shape)


def _ensure_shape(obj):
    """
    Ensures that a tuple or a scalar value is a tuple.
    """
    try:
        return tuple(obj)
    except TypeError:
        return obj,


def _index_tuple(indices):
    """
    Returns a tuple of indices.

    Converts indexed single values to a tuple of size 1.
    """
    if indices is None or (isinstance(indices, int) and indices < 0):
        return indices,
    elif isinstance(indices, int):
        return (indices,)

    return tuple(indices)


def _slice_tuple(slices):
    """
    Handles a single slice by converting it to a tuple of size 1.
    """
    if
