import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32))
</code>
You could also just get it by doing <code>f.__class__.__name__</code> (or <code>ctypes.CFUNCTYPE</code>).

