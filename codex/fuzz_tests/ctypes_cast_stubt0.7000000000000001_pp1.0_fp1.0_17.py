import ctypes
ctypes.cast(m.ctypes.data, ctypes.POINTER(ctypes.c_uint8))[:] = data
</code>
You can also use <code>np.ctypeslib.as_ctypes</code> and <code>ctypes.memmove</code> in the same way. 

