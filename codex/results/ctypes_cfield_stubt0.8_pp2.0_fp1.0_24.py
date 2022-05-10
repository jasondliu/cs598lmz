import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print(ctypes.c_int())


class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

assert type(C()) is C

C1 = ctypes.Structure
C1._fields_ = [('x', ctypes.c_int)]
assert type(C1()) is C1

def ufunc_void(x):
    return

def ufunc_int32(x):
    return 23

def ufunc_float(x):
    return 2.3

def ufunc_complex(x):
    return 2.3j

def ufunc_string(x):
    return "hello"

def ufunc_pyobject(x):
    return 5

def ufunc_object(x):
    return object()

assert ufunc_void(1) is None
assert ufunc_int32(1) == 23
assert ufunc_float(1) == 2.3
assert ufunc_complex(1) == 2.3j
assert ufunc_string(1) == "
