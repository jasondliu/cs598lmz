import ctypes
ctypes.cast(0, ctypes.py_object)

# The above code will raise an exception in Python 3.
# The exception is:
# TypeError: cannot cast c_void_p instance to a pointer to other type
</code>
The reason is that Python 3 uses <code>Py_uintptr_t</code> to cast <code>c_void_p</code> to <code>PyObject*</code> instead of <code>long</code> in Python 2.
So, the following code works in Python 3:
<code>import ctypes
ctypes.cast(0, ctypes.py_object)
</code>

