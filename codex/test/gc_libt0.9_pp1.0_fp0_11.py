import gc, weakref
import numpy as np

def get_array_base(a):
    """
    Returns base array of ndarray pyobject chain, or None if not an ndarray.
    """
    _a = a
    while isinstance(_a, np.ndarray):
        if _a.base is None:
            return _a
        _a = _a.base
    return None

def arange(start, stop, step=1, dtype=None):
    """
    Creates a sequence of numbers with increasing step between each number
    within a given interval.
    """
    if step == 0:
        raise ValueError('step cannot be 0')
    shape = ((stop - start) / step + 0.5).astype(int)
    return np.arange(shape, dtype=np.float64) * step + start

def clamp(x, minimum, maximum):
    """
    Returns array x clamped within the [minimum, maximum] interval.
    """
    return np.minimum(np.maximum(x, minimum), maximum)

