import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFuncPtr(ctypes.CFuncPtr):
    _restype_ = ctypes.c_int
    _argtypes_ = [ctypes.c_int, ctypes.c_int]

ctypes.CFuncPtr = CFuncPtr

def test_array():
    a = (ctypes.c_int * 3)()
    a[0] = 1
    a[1] = 2
    a[2] = 3
    return a

def test_simple_struct():
    s = S()
    s.x = 42
    return s

def test_struct_with_array():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int), ('a', ctypes.c_int * 3)]

    s = S()
    s.x = 42
    s.a[0] = 1
    s.a[1] = 2
    s.a[2] = 3
    return s

def test_struct_with_array_of_structs():
    class S
