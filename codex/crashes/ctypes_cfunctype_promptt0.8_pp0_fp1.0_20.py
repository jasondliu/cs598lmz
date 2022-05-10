import ctypes
PyObject_GetAttrString = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.c_char_p)(("PyObject_GetAttrString", ctypes.pythonapi))
print(ctypes.pythonapi.PyObject_GetAttrString(ctypes.py_object(None),
    ctypes.c_char_p(b'__class__')))
PyObject_GetAttrString(ctypes.py_object(None), ctypes.c_char_p(b'__class__'))
