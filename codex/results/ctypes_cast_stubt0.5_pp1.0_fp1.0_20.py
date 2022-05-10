import ctypes
ctypes.cast(0, ctypes.py_object)

# 错误的转换:
ctypes.cast("hello", ctypes.c_int)

# 可以直接转换:
ctypes.cast(b"hello", ctypes.c_char_p)

# 可以直接转换:
ctypes.cast(b"hello", ctypes.c_void_p)

# 错误的转换:
ctypes.cast(b"hello", ctypes.c_char)

# 可以直接转换:
ctypes.cast(b"hello", ctypes.c_char_p)

# 可以直接转换:
ctypes.cast(b"hello", ctypes.c_void_p)

# 可以直接转换:
ctypes.cast(
