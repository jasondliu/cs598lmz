import ctypes
ctypes.cast(0, ctypes.py_object).value

# not for python3
# ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
# ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
# ctypes.pythonapi.PyCObject_AsVoidPtr(ctypes.py_object(id))


# https://stackoverflow.com/questions/14519177/python-ctypes-set-argtypes-for-c-void-function
# https://docs.python.org/3/library/ctypes.html#fundamental-data-types
# https://docs.python.org/3/library/ctypes.html#ctypes._FuncPtr
# https://stackoverflow.com/questions/8349219/python-ctypes-cant-figure-out-how-to-pass-a-void-pointer-to-a-c-dll
# https://stackoverflow.com/questions/29241844/python-ctypes
