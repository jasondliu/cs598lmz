import ctypes
ctypes.cast(0, ctypes.py_object)

# Test for http://bugs.python.org/issue4604
ctypes.cast(None, ctypes.py_object)

# Test for http://bugs.python.org/issue11588
ctypes.cast(b"", ctypes.py_object)

# Test for http://bugs.python.org/issue1602184
ctypes.cast(b"", ctypes.c_char_p)

# Test for http://bugs.python.org/issue1602184
ctypes.cast(b"", ctypes.c_char_p).value

# Test for http://bugs.python.org/issue1602184
ctypes.cast(None, ctypes.c_char_p)

# Test for http://bugs.python.org/issue1602184
ctypes.cast(None, ctypes.c_char_p).value

# Test for http://bugs.python.org/issue1602184
ctypes.cast(None, ctypes.c_char_p).value = None

# Test for http
