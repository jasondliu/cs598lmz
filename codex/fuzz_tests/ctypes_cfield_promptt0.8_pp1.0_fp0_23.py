import ctypes
# Test ctypes.CField.__repr__
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
x = X()
print(repr(X.a))
print(repr(x.a))

# Test that large ctypes.CField don't segfault the interpreter
if ctypes.sizeof(ctypes.c_longlong)==8 and ctypes.sizeof(ctypes.c_voidp)==8:
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_longlong*(256*1024))]
    x = X()
    print(len(x.a))

if ctypes.sizeof(ctypes.c_longlong)==8 and ctypes.sizeof(ctypes.c_voidp)==4:
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_longlong*(1024*1024))]
    x = X()
    print(len(x.a))
