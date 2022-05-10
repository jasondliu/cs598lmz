import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes模块的pythonapi
# ctypes.pythonapi.Py_InitModule4.restype = ctypes.py_object
# ctypes.pythonapi.Py_InitModule4.argtypes = [ctypes.c_char_p, ctypes.py_object, ctypes.c_char_p, ctypes.py_object, ctypes.c_int]
# ctypes.pythonapi.Py_InitModule4(b'hello', hello.methods, b'A hello world extension module.', None, PYTHON_API_VERSION)

# 使用ctypes模块的pythonapi
# ctypes.pythonapi.Py_InitModule4_64.restype = ctypes.py_object
# ctypes.pythonapi.Py_InitModule4_64.argtypes = [ctypes.c_char_p, ctypes.py_object, ctypes.c_char_p, ctypes.py_object, ctypes.c_int]
#
