import ctypes
# Test ctypes.CFUNCTYPE(None, ctypes.c_char_p)
def func(value):
    print('func: %s' % value)

# ctypes.pythonapi.Py_InitModule4.argtypes = (ctypes.c_char_p, ctypes.POINTER(PyMethodDef), ctypes.c_char_p, ctypes.py_object, ctypes.c_int)
# ctypes.pythonapi.Py_InitModule4.restype = ctypes.py_object
# module = ctypes.pythonapi.Py_InitModule4(b'foo', None, None, None, PYTHON_API_VERSION)
# assert module
# assert PyModule_Check(module)
# assert PyModule_GetDict(module)
# assert PyModule_AddObject(module, b'func', PyCFunction_NewEx(&amp;cfunc, None, module)) == 0
# assert PyErr_Occurred() == None
# Py_DECREF(module)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char
