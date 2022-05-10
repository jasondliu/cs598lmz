import ctypes
ctypes.cast("abc", ctypes.c_char_p).value
# 'abc'
