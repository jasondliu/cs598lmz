import ctypes
ctypes.cast(ctypes.c_void_p(0x4), ctypes.py_object).value

# This is a bit more complicated, but it's the same thing.
# It's just a way to get the address of a Python object.
import ctypes
ctypes.cast(ctypes.py_object(None), ctypes.c_void_p).value
</code>

