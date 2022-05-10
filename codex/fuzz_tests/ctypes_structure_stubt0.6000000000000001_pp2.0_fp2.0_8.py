import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float

class T(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class U(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_char_p

class V(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_wchar_p

class W(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.POINTER(ctypes.c_int)

class X(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.POINTER(ctypes.c_char_p)

class Y(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.POINTER(ctypes.c_wchar_p)

def make_struct_test(obj):
    def test_struct(self):
       
