import ctypes
ctypes.cast(p, ctypes.py_object).value = x
</code>
Note that this simply directly allocates memory and points <code>p</code> to it.  A C function will be able to treat <code>p</code> exactly as if it were a normal C pointer to an int object, though.
If you wanted a pointer to a name that you can use within Python, you could do something like this:
<code>x = ctypes.c_int(42)
print(x.__name__)
</code>

