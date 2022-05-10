import ctypes
ctypes.cast(myobj, ctypes.py_object).value

# alternatively:
from ctypes.wintypes import HANDLE
get_object = ctypes.pythonapi.PyCObject_AsVoidPtr
get_object.restype = ctypes.c_void_p
get_object.argtypes = [ctypes.py_object]
print(get_object(myobj))

# only for Python 2.x (but with tp_repr and tp_str flags the same for PyObject_Print)
print(ctypes.cast(myobj, ctypes.POINTER(ctypes.py_object)).contents.value)

if '__main__' == __name__:
    import doctest
    doctest.testmod()
