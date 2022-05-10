import ctypes
ctypes.cast(1, ctypes.py_object)

# TypeError: an integer is required

ctypes.cast(1.0, ctypes.py_object)

# TypeError: a float is required

ctypes.cast("hello", ctypes.py_object)

# TypeError: a string is required

ctypes.cast(b"hello", ctypes.py_object)

# TypeError: a bytes-like object is required, not 'str'

ctypes.cast(b"hello", ctypes.c_char_p)

# <ctypes.c_char_p object at 0x7f0e07b8f0a0>

ctypes.cast(b"hello", ctypes.c_char_p).value

# b'hello'

ctypes.cast(b"hello", ctypes.c_wchar_p)

# <ctypes.c_wchar_p object at 0x7f0e07b8f0a0>

ctypes.cast(b"hello", ctypes.c_wchar_p
