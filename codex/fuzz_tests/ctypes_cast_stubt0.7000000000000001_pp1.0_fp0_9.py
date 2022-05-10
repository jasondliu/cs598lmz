import ctypes
ctypes.cast(0x12345678, ctypes.py_object).value

# Output:
305419896
</code>
This is the same as you would get for <code>PyLong_FromVoidPtr</code>; in fact, one might think this is the same way it works internally. But I don't know.
Anyway, don't do that. There is no good reason to extract an object's address and convert it to a Python integer.

