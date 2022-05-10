import ctypes
ctypes.cast("abc", ctypes.c_char_p).value
# 'abc'
ctypes.cast("abc", ctypes.c_char_p).contents
# 'abc'
ctypes.cast("abc", ctypes.c_char_p).value.contents
# 'abc'
ctypes.cast("abc", ctypes.c_char_p).value.value
# 'abc'
ctypes.cast("abc", ctypes.POINTER(ctypes.c_char)).value
# 'abc'
ctypes.cast("abc", ctypes.POINTER(ctypes.c_char)).contents
# 'abc'
ctypes.cast("abc", ctypes.POINTER(ctypes.c_char)).value.contents
# 'abc'
ctypes.cast("abc", ctypes.POINTER(ctypes.c_char)).value.value
# 'abc'
</code>


A:

If you have a Python 2.x string <code>"abc"</code> and you want a pointer to it, you can just hand the Python string to ctypes, and it will
