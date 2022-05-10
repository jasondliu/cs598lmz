import ctypes
# Test ctypes.CFUNCTYPE()
assert ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
print('pass')

# Test ctypes.c_ubyte
assert ctypes.c_ubyte
print('pass')

# Test ctypes.c_void_p
assert ctypes.c_void_p
print('pass')
