import ctypes
# Test ctypes.CField
assert ctypes.CField.from_address.im_class == ctypes.CField
assert ctypes.CField.from_param.im_class == ctypes.CField
# Test ctypes.c_ubyte
assert ctypes.c_ubyte(-1) == 0xff
assert ctypes.c_ubyte(8) == 8
# Test ctypes.c_byte
assert ctypes.c_byte(-1) == -1
assert ctypes.c_byte(0x80) == -0x80
