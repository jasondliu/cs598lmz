import ctypes
ctypes.cast(ctypes.addressof(my_struct), ctypes.POINTER(my_struct)).contents.x
</code>

