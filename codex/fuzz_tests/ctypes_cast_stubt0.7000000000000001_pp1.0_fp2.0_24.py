import ctypes
ctypes.cast(id(my_func), ctypes.py_object).value
</code>
which gives you a function object. You can also use the <code>inspect</code> module to get the source code of the function, which includes the <code>def</code> line.

