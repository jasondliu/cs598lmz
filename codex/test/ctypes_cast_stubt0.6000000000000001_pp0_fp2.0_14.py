import ctypes
ctypes.cast(0, ctypes.py_object)

# This causes a segfault on the Mac.
# ctypes.cast(0, ctypes.py_object).__class__

ctypes.cast(0, ctypes.py_object).__class__.__name__

class X(object):
    pass

