import gc, weakref

from . import _util
from . import _core
from . import _core_internal
from . import _ffi
from . import _numba_types


def _validate_type(type):
    if not isinstance(type, _numba_types.Type):
        raise TypeError("expected numba type, got %s" % (type,))
    if not _numba_types.is_precise_type(type):
        raise TypeError("expected precise type, got %s" % (type,))

def _validate_types(types):
    for type in types:
        _validate_type(type)

class _Bounds(object):
    def __init__(self):
        self.min = self.max = None

    def update(self, value):
        if self.min is None or value < self.min:
            self.min = value
        if self.max is None or value > self.max:
            self.max = value

class _BoundsMap(object):
    def __init__(self,
