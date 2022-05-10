import ctypes
ctypes.cast(0, ctypes.py_object)

# imports for Python2
try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

# import for PyQt5
