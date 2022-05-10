import ctypes
ctypes.cast(0, ctypes.py_object).value

# ctypes.cast(0, ctypes.py_object).value
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-4-a8d4d4f9c7f9> in <module>()
# ----> 1 ctypes.cast(0, ctypes.py_object).value

# TypeError: NULL pointer access

# ctypes.cast(0, ctypes.py_object).value = 42
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-5-b8c8e9a8e9a7> in <module>()
# ----> 1 ctypes.cast(0, ctypes.py_object).value = 42

# TypeError: NULL pointer access

# ctypes.cast(0, ctypes.py_object).value
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-6-a8d4d4f9c
