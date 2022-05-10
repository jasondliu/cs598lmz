import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes模块可以调用C语言的库函数，比如libc中的printf函数
libc = ctypes.CDLL(None)
printf = libc.printf
printf('Hello, %s\n', b'world')

# 使用ctypes模块可以调用C语言的库函数，比如libc中的printf函数
libc = ctypes.CDLL(None)
printf = libc.printf
printf('Hello, %s\n', b'world')

# 使用ctypes模块可以调用C语言的库函数，比如libc中的printf函数
libc = ctypes.CDLL(None)
printf = libc
