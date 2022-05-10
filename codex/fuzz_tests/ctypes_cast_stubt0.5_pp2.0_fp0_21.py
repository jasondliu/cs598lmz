import ctypes
ctypes.cast(1, ctypes.py_object)

# TypeError: an integer is required

ctypes.cast(1.0, ctypes.py_object)

# TypeError: a float is required

ctypes.cast('hello', ctypes.py_object)

# TypeError: a bytes-like object is required, not 'str'

ctypes.cast(b'hello', ctypes.py_object)

# b'hello'

ctypes.cast(bytearray(b'hello'), ctypes.py_object)

# bytearray(b'hello')

ctypes.cast(b'hello', ctypes.c_char_p)

# b'hello'

ctypes.cast('hello', ctypes.c_char_p)

# b'hello'

ctypes.cast(bytearray(b'hello'), ctypes.c_char_p)

# b'hello'

ctypes.cast(1, ctypes.c_char_p)

# TypeError: an integer is required


