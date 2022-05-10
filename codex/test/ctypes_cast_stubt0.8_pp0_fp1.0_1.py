import ctypes
ctypes.cast(0, ctypes.py_object);
# sigsys() gets called because libffi calls PyPy_FatalError() when it fails to convert types
