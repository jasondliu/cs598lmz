import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
That way, you can use <code>ctypes.cast</code> to convert between different pointer types, as long as you have the C types defined in your program.

