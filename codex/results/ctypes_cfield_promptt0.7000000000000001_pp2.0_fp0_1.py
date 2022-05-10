import ctypes
# Test ctypes.CField
class A(ctypes.Structure):
    _fields_ = [('foo', ctypes.CField)]
# Test ctypes.Array
class B(ctypes.Structure):
    _fields_ = [('foo', ctypes.Array)]
# Test ctypes.CFuncPtr
class C(ctypes.Structure):
    _fields_ = [('foo', ctypes.CFuncPtr)]
# Test ctypes.BigEndianStructure
class D(ctypes.BigEndianStructure):
    _fields_ = [('foo', ctypes.c_int)]
# Test ctypes.LittleEndianStructure
class E(ctypes.LittleEndianStructure):
    _fields_ = [('foo', ctypes.c_int)]
# Test ctypes.PYFUNCTYPE
def func(foo):
    return foo
ctypes.PYFUNCTYPE(None, None)(func)
# Test ctypes.c_bool
ctypes.c_bool()
# Test ctypes.c_buffer
ctypes.c_buffer()
# Test ctypes.c
