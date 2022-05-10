import ctypes
# Test ctypes.CFUNCTYPE
# Only the return type is significant for ctypes, the arguments
# can be anything at all.
PyObject = ctypes.py_object
f = ctypes.CFUNCTYPE(PyObject)(lambda x: x)
