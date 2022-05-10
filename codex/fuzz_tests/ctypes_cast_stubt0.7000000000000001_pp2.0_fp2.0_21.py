import ctypes
ctypes.cast(ptr, ctypes.py_object).value = my_new_value
</code>
Note that the above assumes that <code>my_new_value</code> is a Python object. If it's not, you may have to write some other logic to convert it to a Python object.

