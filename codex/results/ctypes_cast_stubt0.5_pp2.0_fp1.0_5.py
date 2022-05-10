import ctypes
ctypes.cast(a, ctypes.c_void_p).value

# or 

ctypes.addressof(a)

# or

id(a)
</code>

