import ctypes
# Test ctypes.CFUNCTYPE
PyObject_GetAttrString = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.c_char_p)(("PyObject_GetAttrString", ctypes.pythonapi))
PyObject_GetAttrString.restype = ctypes.py_object
print(PyObject_GetAttrString(ctypes.py_object(1), b'__class__').value.value.value)
# Test ctypes.cast()
# PyObject_GetAttrString = ctypes.cast(("PyObject_GetAttrString", ctypes.pythonapi), ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.c_char_p))
# print(PyObject_GetAttrString(ctypes.py_object(1), b'__class__').value.value.value)
# Test ctypes.POINTER()
PyObject_GetAttrString = ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object
