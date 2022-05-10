import ctypes
ctypes.cast(ctypes.c_ulong(1).value, ctypes.py_object).value
</code>
will produce
<code>1
</code>
It's not a truly weird result, we are simply accessing the C object value. It's not a Python object, that is why it's not being interpreted as an int by python.
This could be useful to perform some low level operations on the memory (e.g. byte swap), just be aware that you are addressing the C object and not an equivalent Python object.

