import ctypes
ctypes.cast(ctypes.py_object(np.float32(0.0)), ctypes.c_void_p).value

# to get the value out of the pointer:
ctypes.POINTER(ctypes.c_float)[0].value
#Output: 0.0
</code>

