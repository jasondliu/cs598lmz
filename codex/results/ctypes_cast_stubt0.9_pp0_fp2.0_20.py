import ctypes
ctypes.cast(m.mv, ctypes.POINTER(ctypes.c_void_p))
</code>
If you use struct.unpack or struct.pack you can use <code>m.mv</code> directly.

