import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

# Test ctypes.CFuncPtr
def handler(a, b, c):
    print(a, b, c)

handler_p = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)(handler)

# Test ctypes.CStruct
class A(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

# Test ctypes.CUnion
class B(ctypes.Union):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

# Test ctypes.CArray
class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int * 2)]

# Test ctypes.CString
class D(
