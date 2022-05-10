import ctypes
# Test ctypes.CFUNCTYPE()
try:
    CFUNCTYPE = ctypes.CFUNCTYPE
except AttributeError:
    pass
else:
    c_string_p = ctypes.c_char_p
    c_int = ctypes.c_int
    c_double = ctypes.c_double
    c_void_p = ctypes.c_void_p
    def echo(s):
        return s
    func = CFUNCTYPE(c_string_p, c_string_p)(echo)
