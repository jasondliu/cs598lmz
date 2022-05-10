import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a workaround for a bug in the Python interpreter:
#  http://bugs.python.org/issue15881#msg170215
try:
    ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
    ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]
except AttributeError:
    # This function is not available on Windows and on many Linux systems.
    pass
else:
    def _as_parameter_ (self):
        """Return self, which is needed to convert objects to function parameters"""
        return self
    ctypes.py_object.__repr__ = _as_parameter_

# This is a workaround for a bug in the Python interpreter:
#  http://bugs.python.org/issue15881#msg170215
try:
    ctypes.pythonapi.PyCapsule_GetName.restype = ctypes.c_
