import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('c', ctypes.c_char)]

ctypes.CChar = type(C.c)

class S(ctypes.Structure):
    _fields_ = [('c', ctypes.c_char_p)]


if __name__ == '__main__':
    import support
    support.run_unittest(__name__)
