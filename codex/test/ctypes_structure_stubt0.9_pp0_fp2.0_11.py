import ctypes

class S(ctypes.Structure):
    x = [("foo", ctypes.c_char * 2),
         ("bar", ctypes.c_char * 3)]
    x = [("foo", ctypes.c_char * 2),
         ("bar", ctypes.c_char * 3)]

S()
