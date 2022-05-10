import ctypes
# Test ctypes.CFUNCTYPE
def cb(x, y):
    return x * y

cb_t = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cb_f = cb_t(cb)

cb_f(2, 3)

# Test ctypes.c_byte (signed char)
ctypes.c_byte(-128)
ctypes.c_byte(0)
ctypes.c_byte(127)

# Test ctypes.c_ubyte (unsigned char)
ctypes.c_ubyte(0)
ctypes.c_ubyte(255)

# Test ctypes.c_short (short)
ctypes.c_short(-32768)
ctypes.c_short(0)
ctypes.c_short(32767)

# Test ctypes.c_ushort (unsigned short)
ctypes.c_ushort(0)
ctypes.c_ushort(65535)

# Test ctypes.c_int (int)
ct
