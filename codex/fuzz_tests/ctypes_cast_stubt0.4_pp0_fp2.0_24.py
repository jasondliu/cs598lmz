import ctypes
ctypes.cast(ctypes.c_void_p(id(obj)), ctypes.py_object).value
</code>
I'm not sure if this is a good idea in general, but it works.

