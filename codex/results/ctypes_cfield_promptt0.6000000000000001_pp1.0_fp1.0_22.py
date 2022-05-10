import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
assert X.a == X._fields_[0][1]
# Test ctypes.Field
class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
assert Y.a == Y._fields_[0][1]
# Test ctypes.CFuncPtr
assert ctypes.CFuncPtr is ctypes._CFuncPtr
def callback(a):
    return a
assert ctypes.CFuncPtr(callback) == ctypes.CFUNCTYPE(ctypes.c_int)(callback)
# Test ctypes.MemFunPtr
class Z(ctypes.Structure):
    _fields_ = [("func", ctypes.CFUNCTYPE(ctypes.c_int))]
assert ctypes.MemFunPtr(Z.func) == ctypes.CFUNCTYPE(ctypes.c_int)(Z.func)
# Test ctypes.Union
assert ctypes.Union is ctypes._Union

#
