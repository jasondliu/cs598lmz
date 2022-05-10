import ctypes
ctypes.cast(5, ctypes.py_object)
# ...anywhere that a PyObject* is expected,
# you can also supply an int, just as you could before.

# But something *new* can be done:
ctypes.cast('Hello World', ctypes.py_object)
# ...you can now supply a (non-null) pointer to
# a null-terminated SIP string without crashing.

# You can also go back the other way:
ctypes.cast('Hello World', ctypes.c_char_p).value
# This does NOT return 'Hello World' anymore, but a pointer to
# a Python str object in memory, this pointer cannot be used
# to do anything useful.
</code>

