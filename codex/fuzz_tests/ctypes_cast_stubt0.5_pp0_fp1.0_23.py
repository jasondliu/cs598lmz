import ctypes
ctypes.cast(p, ctypes.py_object).value
</code>

If you need to use the same pointer from multiple interpreters, then you have to use the same Python interpreter object in each of them. You can do this by creating a custom Python interpreter and passing it to the other interpreters.
See the <code>Py_NewInterpreter()</code> documentation.

