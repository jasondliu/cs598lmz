import ctypes
ctypes.cast(0, ctypes.py_object)

# The following statement is necessary to make the above line work
# (without it, the above line will cause an exception).
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]

# The following code is based on the C++ code from the following web page:
# http://www.boost.org/doc/libs/1_60_0/libs/python/doc/html/tutorial/tutorial/exposing.html

# The following code is based on the C++ code from the following web page:
# http://www.boost.org/doc/libs/1_60_0/libs/python/doc/html/tutorial/tutorial/exposing.html

# The following code is based on the C++ code from the following web page:
# http://www.boost.org/doc/libs/1_60
