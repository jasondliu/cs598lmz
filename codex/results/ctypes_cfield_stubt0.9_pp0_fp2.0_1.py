import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class StablePtr (object):
    _type_ = "stableptr"

class ForeignPtr (object):
    def __init__(self, ptr, finalizer=None):
        if isinstance(ptr, _CData):
            self._ptr = ptr
            self._finalizer = None
        else:
            if isinstance(ptr, Closure):
                self._ptr = _get_closure_func(ptr)
                self._finalizer = _get_closure_finalizer(ptr)
            elif not isinstance(ptr, _CData):
                raise TypeError("ptr must be a ctypes pointer or a ctypes callback")
            else:
                self._ptr = ptr
                self._finalizer = finalizer

    @property
    def finalizer(self):
        return self._finalizer
    
    @finalizer.setter
    def finalizer(self, finalizer):
        if self._finalizer is not None:
            raise Exception("cannot modify finalizers")
        self._finalizer = finalizer

    @property
    def _as_parameter_(self
