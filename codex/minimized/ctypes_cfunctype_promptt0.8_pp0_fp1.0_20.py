import ctypes
PyObject_GetAttrString = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.c_char_p)(("PyObject_GetAttrString", ctypes.pythonapi))
print(PyObject_GetAttrString(ctypes.py_object(1), b'__class__').value.value.value)
