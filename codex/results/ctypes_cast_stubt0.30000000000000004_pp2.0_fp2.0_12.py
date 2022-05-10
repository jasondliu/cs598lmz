import ctypes
ctypes.cast(0, ctypes.py_object).value

# The following is the same as the above, but uses ctypes.pythonapi instead of
# ctypes.cdll.pythonapi.  The difference between the two is that when
# Python is built in release mode, cdll.pythonapi cannot be used.
ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyCObject_AsVoidPtr(ctypes.py_object(0))

# Test ctypes.c_buffer, ctypes.c_wchar_p and ctypes.c_char_p
ctypes.c_buffer("abc")
ctypes.c_wchar_p("abc")
ctypes.c_char_p("abc")

# Test ctypes.c_void_p(obj)
ctypes.c_void_p(ctypes.py_object(0))

# Test ctypes.c_
