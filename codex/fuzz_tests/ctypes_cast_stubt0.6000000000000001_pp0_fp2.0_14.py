import ctypes
ctypes.cast(0, ctypes.py_object)

# This causes a segfault on the Mac.
# ctypes.cast(0, ctypes.py_object).__class__

ctypes.cast(0, ctypes.py_object).__class__.__name__

class X(object):
    pass

ctypes.cast(X(), ctypes.py_object).__class__

ctypes.cast(X(), ctypes.py_object).__class__.__name__

# issue7242
ctypes.cast(1, ctypes.py_object)
ctypes.cast(1.0, ctypes.py_object)
ctypes.cast(1+2j, ctypes.py_object)
ctypes.cast('x', ctypes.py_object)
ctypes.cast(u'x', ctypes.py_object)
ctypes.cast({}, ctypes.py_object)
ctypes.cast((), ctypes.py_object)
ctypes.cast([], ctypes.py_object)
ctypes.cast(object(),
