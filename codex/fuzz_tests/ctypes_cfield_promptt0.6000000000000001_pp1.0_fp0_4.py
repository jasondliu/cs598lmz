import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]

class D(ctypes.Union):
    _fields_ = [("bar", ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [("baz", ctypes.c_int)]

for tp in (C, D, E):
    print(tp)
    print("This is a real Structure:", isinstance(tp, ctypes.Structure))
    print("This is a real Union:", isinstance(tp, ctypes.Union))
    print("This is a C type:", isinstance(tp, ctypes.CField))
    print("This is a C type:", issubclass(tp, ctypes.CField))
    print("This is a C type:", issubclass(tp, ctypes.c_int))
    print("This is a C type:", issubclass(tp, ctypes.c_void_p))
    print("This is a C type:", issubclass(ct
