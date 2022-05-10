import ctypes
# Test ctypes.CFUNCTYPE is callable
try:
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int)) # TypeError: not a valid native integer datatype.
    raise ctypes.ArgumentError("should not be reached")
except TypeError:
    pass

# Test ctypes.Structure is callable
class X(ctypes.Structure):
    pass
class Y:
    __metaclass__ = X

assert Y._fields_ == []

try:
    class Z:
        __metaclass__ = X()
    raise RuntimeError("should not be reached")
except AttributeError:
    pass

# Issue #20739: Call `__getattr__` on `ctypes.Structure`
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    def __getattr__(self, name):
        if name == 'b':
            return 7
        raise AttributeError

assert X().a == 0
assert X().b == 7

