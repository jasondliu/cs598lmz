import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p
    _fields_ = [('x', ctypes.c_void_p)]
    __slots__ = [('x', ctypes.c_void_p)]

if __name__ == '__main__':
    import ctypes
    ctypes.create_string_buffer(b"test")
