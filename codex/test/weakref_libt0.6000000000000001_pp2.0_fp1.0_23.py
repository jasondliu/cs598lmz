import weakref

from numpy import zeros, empty_like, ones, asarray
from numpy.linalg import norm

from gnumpy import dot, zeros_like, sum
from gnumpy.gnumpy import N
from gnumpy.memoize import memoize


def _broadcast_shape(shapes):
    bshape = []
    for i, s in enumerate(shapes):
        if len(s) == 1:
            bshape.append(s[0])
        else:
            bshape.append(s[i])
    return bshape


class Tensor(object):
    def __init__(self, data, dtype=None):
        if isinstance(data, N):
            if dtype is not None:
                raise ValueError('dtype must be None if data is a gnumpy array')
            self._data = data
        else:
            if dtype is None:
                dtype = data.dtype
            self._data = N(data, dtype)

    @property
    def shape(self):
        return self._data.shape
