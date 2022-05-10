import ctypes
ctypes.cast(ctypes.pointer(c_int(0x12345678)), ctypes.POINTER(ctypes.c_ubyte))

#@ctypes.cast(ctypes.pointer(ctypes.c_int(0x12345678)), ctypes.POINTER(ctypes.c_ubyte))
buffer(ctypes.c_int(0x12345678))

s = 'This is the array.'
a = array.array('c', s)

a.fromstring(s)
