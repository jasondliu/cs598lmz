import ctypes
ctypes.cast(ctypes.addressof(pointer_to_integer), ctypes.POINTER(ctypes.c_float))
</code>
and then use the pointer.

