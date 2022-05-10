import ctypes
ctypes.cast(1, ctypes.c_void_p).value

# if ctypes.cast(1, ctypes.c_void_p).value &gt; 2**32:
#     print("64-bit")
# else:
#     print("32-bit")
