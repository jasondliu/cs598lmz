import ctypes
ctypes.cast(ids, ctypes.py_object).value = idcount
</code>
So that all threads in majority of the case see the same value.

