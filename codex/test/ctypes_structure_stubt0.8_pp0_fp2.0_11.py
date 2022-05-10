import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    s = ctypes.c_char_p
    s2 = ctypes.c_wchar_p
    s3 = ctypes.c_char * 4

S_ = ctypes.c_char * 16

