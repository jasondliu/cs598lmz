import ctypes
ctypes.cast(0, ctypes.py_object).value

# In [11]: ctypes.cast(0, ctypes.py_object).value
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-11-4d4c7b2f0b9d> in <module>()
# ----> 1 ctypes.cast(0, ctypes.py_object).value

# ValueError: NULL pointer access
# In [12]: ctypes.cast(0, ctypes.py_object).value = 1
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-12-e7f1c9e9a8d1> in <module>()
# ----> 1 ctypes.cast(0, ctypes.py_object).value = 1

# ValueError: NULL pointer access
# In [13]: 

# In [13]: 

# In [13]: 

# In [13]: 

# In [13]: 

# In [13]: 

