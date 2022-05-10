import ctypes
# Test ctypes.CField.
libc = ctypes.cdll.LoadLibrary(None)
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int, 6)]

# Internal fields should not be exposed, this is for backwards compatibility
# with Python 2.4.
import sys
if sys.version_info >= (2, 5):
    raises(AttributeError, "X.a")
    assert X.a.value == 0
    assert X.a.offset == 0
    assert X.a.size == 4
    assert X.a.bits == 6
    assert X.a.length == 1
    assert X.a.type == ctypes.c_int

X.a.value = 63
assert X.a.value == 63

# Test whether _fields_ can be used without _pack_
class Y(ctypes.Structure):
    _fields_ = [("c", ctypes.c_int)]

assert Y._pack_ == 1

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_
