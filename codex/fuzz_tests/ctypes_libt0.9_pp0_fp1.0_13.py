import ctypes
ctypes.cast(buffer, ctypes.POINTER(ctypes.c_char * 4)).contents

# create void pointer with buffer
b = bytearray(b'\x01\x02\x03\x04')
vp = ctypes.cast(b, ctypes.c_void_p)

# cast void pointer to bytearray and get pointer
vp2 = ctypes.cast(vp, ctypes.POINTER(ctypes.c_ubyte * 4))
vp2.contents
