import ctypes
ctypes.cast(ctypes.c_int, ctypes.c_int)
ctypes.cast(ctypes.c_int(0x1234), ctypes.c_short)
ctypes.cast(ctypes.c_int(0x1234), ctypes.c_char)
ctypes.cast(ctypes.c_float(1.2345), ctypes.c_int)

print "* 4.3.3 ctypes: - c_void_p"
ctypes.cast(None, ctypes.c_void_p)
ctypes.cast(0x1234, ctypes.c_void_p)
ctypes.cast(ctypes.pointer(ctypes.c_int(0x1234)), ctypes.c_void_p)
ctypes.cast(0x1234, ctypes.c_char).value
ctypes.cast(0x1234, ctypes.c_char * 100)

print "* 4.3.4 ctypes: - sizeof"
ctypes.sizeof(ctypes.c_int)
ctypes.sizeof(ct
