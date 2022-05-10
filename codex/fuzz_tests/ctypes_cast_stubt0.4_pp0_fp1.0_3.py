import ctypes
ctypes.cast(a, ctypes.POINTER(ctypes.c_int))
</code>
This will give you a <code>ctypes.POINTER(ctypes.c_int)</code> object that you can use to access the memory.

