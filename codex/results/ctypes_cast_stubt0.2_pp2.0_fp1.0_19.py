import ctypes
ctypes.cast(0, ctypes.py_object).value

# ctypes.cast(0, ctypes.py_object).value
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-11-9a8d1a8b8d2b> in <module>
# ----> 1 ctypes.cast(0, ctypes.py_object).value

# AttributeError: 'NoneType' object has no attribute 'value'

# ctypes.cast(0, ctypes.py_object).value = 'string'
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-12-c6f5a5b7c0d1> in <module>
# ----> 1 ctypes.cast(0, ctypes.py_object).value = 'string'

# AttributeError: 'NoneType' object has no attribute 'value'

# ctypes.cast(0, ctypes.py_object).value = 'string'
# ---------------------------------------------------------------------------
# AttributeError                           
