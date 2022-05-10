import ctypes
# Test ctypes.CField
ctypes.CField(ctypes.c_int, 'a')
ctypes.CField(ctypes.c_int, 'a', 1)
ctypes.CField(ctypes.c_int, 'a', 1, True)
ctypes.CField(ctypes.c_int, 'a', 1, True, 'd')
ctypes.CField(ctypes.c_int, 'a', 1, True, 'd', 'e')
ctypes.CField(ctypes.c_int, 'a', 1, True, 'd', 'e', 'f')
ctypes.CField(ctypes.c_int, 'a', 1, True, 'd', 'e', 'f', 'g')
ctypes.CField(ctypes.c_int, 'a', 1, True, 'd', 'e', 'f', 'g', 'h')
ctypes.CField(ctypes.c_int, 'a', 1, True, 'd', 'e', 'f', 'g', 'h', 'i')
ctypes.CField(ctypes.
