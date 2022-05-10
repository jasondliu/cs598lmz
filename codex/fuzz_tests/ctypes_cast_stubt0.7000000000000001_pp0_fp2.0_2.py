import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
you get a <code>TypeError</code> which is pretty clear:
<code>TypeError: int is not a Python object
</code>
The same happens for <code>ctypes.c_void_p(0)</code>:
<code>TypeError: void pointer is not a Python object
</code>

