import ctypes
# Test ctypes.CField
ctypes.sizeof(ctypes.c_int)
ctypes.sizeof(ctypes.CField)
ctypes.sizeof(ctypes.Union)
ctypes.sizeof(ctypes.UnionType(ctypes.CField("a", ctypes.c_int),
                               ctypes.CField("b", ctypes.c_char, 5)))
ctypes.sizeof(ctypes.UnionType(ctypes.CField("a", ctypes.c_int),
                               ctypes.CField("b", ctypes.c_char, 5),
                               ctypes.CField("c", ctypes.c_longlong)))
ctypes.sizeof(ctypes.UnionType(ctypes.CField("a", ctypes.c_int),
                               ctypes.CField("b", ctypes.c_char, 5),
                               ctypes.CField("c", ctypes.c_longlong),
                               ctypes.CField("d", ctypes.c_int)))
ctypes.sizeof(ctypes.UnionType(ctypes.C
