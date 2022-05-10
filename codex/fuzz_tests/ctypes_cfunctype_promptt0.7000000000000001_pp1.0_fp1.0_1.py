import ctypes
# Test ctypes.CFUNCTYPE()
def func(arg):
    print arg

CFUNCTYPE(None, c_int)(func)(42)

# Test ctypes.POINTER()
class S(Structure):
    _fields_ = [("y", c_int)]

s = S()
print POINTER(S).in_dll(ctypes.pythonapi, "PyCObject_FromVoidPtr").restype(py_object)(pointer(s), None)

# Test ctypes.pointer()
p = pointer(s)
print p.contents
print p.contents.y

# Test ctypes.addressof()
print addressof(s)

# Test ctypes.alignment()
print alignment(S)
print alignment(c_int)

# Test ctypes.byref()
def func2(arg):
    print arg
CFUNCTYPE(None, POINTER(c_int))(func2)(byref(c_int(42)))
