import ctypes
ctypes.cast(ctypes.c_int(), ctypes.c_char_p)

MemoryError: cast() argument 1 must be a pointer, not int
</code>


A:

This is an often-seen mistake.  You have confused the name of a data type (which always begins with a capital letter) with the actual data.
The correct way to convert an integer to a char pointer is to use the <code>ctypes.byref</code> function.  This takes a Python value and turns it into a pointer to that value.  For example:
<code>import ctypes
ctypes.cast(ctypes.byref(ctypes.c_int()), ctypes.c_char_p)
</code>

