import ctypes
ctypes.cast(0, ctypes.py_object)

print(ctypes.cast(0, ctypes.py_object))
</code>
prints
<code>c_void_p(0)
</code>
but
<code>import ctypes
ctypes.cast('', ctypes.py_object)

print(ctypes.cast('', ctypes.py_object))
</code>
prints
<code>c_void_p(0x4a4d08)
</code>
What does the <code>0x4a4d08</code> in the second example mean?


A:

<code>0</code> is a C null pointer, but <code>''</code> is a Python empty string, which is a valid Python object.  <code>ctypes</code> is therefore creating a pointer to that string.  In Python 3.x, strings are immutable, so the pointer can be safely cached and reused every time you cast an empty string to <code>py_object</code>.  In Python 2.x, strings were mutable, so a new <code>py_
