import ctypes
ctypes.cast(ctypes.c_char_p(addr), ctypes.POINTER(ctypes.c_ulong)).contents
</code>

