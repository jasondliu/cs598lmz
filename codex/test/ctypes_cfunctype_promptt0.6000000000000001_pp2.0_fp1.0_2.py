import ctypes
# Test ctypes.CFUNCTYPE(None)
# ctypes.c_int.in_dll(ctypes.pythonapi, 'Py_IsInitialized').value
print(ctypes.c_int.in_dll(ctypes.pythonapi, 'Py_IsInitialized').value)
# Test ctypes.CFUNCTYPE(ctypes.c_int)
# ctypes.c_int.in_dll(ctypes.pythonapi, 'Py_IsInitialized').value
print(ctypes.c_int.in_dll(ctypes.pythonapi, 'Py_IsInitialized').value)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
# ctypes.pythonapi.PyObject_IsTrue(0)
print(ctypes.pythonapi.PyObject_IsTrue(0))
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)
# ctypes.py_object().in_dll(ctypes.pythonapi, 'Py_True').value
