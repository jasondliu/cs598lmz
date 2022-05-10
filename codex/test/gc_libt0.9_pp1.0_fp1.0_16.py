import gc, weakref

def _isempty(x):
    return x is None or (hasattr(np, 'isscalar') and np.isscalar(x) and not np.isfinite(x))

def _builtin_norm(shape,kwargs):
    scale = kwargs.get('scale', 1.0)
    return scale * np.random.randn(*shape)


class Variable(object):
    __slots__ = ['_ctx', '_creator', '_shape', '_ndim']

    def __init__(self,shape,data, creator=None):
        self._ctx = Context
        self._shape = shape
        self._data = data
        self._size = len(self._data.reshape(len(self._data)))
        self._ndim = len(shape)
        self._creator = None
    def __lt__(self, y):
        return zeros_like(self) < y
    def __le__(self, y):
        return zeros_like(self) <= y
