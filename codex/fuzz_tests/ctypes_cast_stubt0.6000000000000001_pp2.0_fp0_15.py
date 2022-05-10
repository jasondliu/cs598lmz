import ctypes
ctypes.cast(ctypes.addressof(s), ctypes.POINTER(ctypes.c_long))[0]
# Out[65]: 18
ctypes.cast(ctypes.addressof(s), ctypes.POINTER(ctypes.c_long))[1]
# Out[66]: 0
ctypes.cast(ctypes.addressof(s), ctypes.POINTER(ctypes.c_long))[2]
# Out[67]: 0
ctypes.cast(ctypes.addressof(s), ctypes.POINTER(ctypes.c_long))[3]
# Out[68]: 0

# so the actual value of the bit field is 18
</code>

