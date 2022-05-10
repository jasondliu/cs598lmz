import ctypes
ctypes.cast(p, ctypes.POINTER(ctypes.c_size_t))[0] = 3.14
print(ctypes.cast(p, ctypes.POINTER(ctypes.c_size_t))[0])
</code>
Result: gc failed collecting world 1

