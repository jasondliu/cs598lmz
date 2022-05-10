import ctypes
ctypes.cast(ctypes.pointer(my_struct), ctypes.POINTER(ctypes.c_char * 16)).contents.raw
# b'\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
</code>

