import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# 将一个整数转换为无符号的字符
n = -37
m = ctypes.c_ubyte(n).value

# 将一个字符串转换为字节
s = b'hello world'
b = s.decode('utf-8')

# 将一个字节转换为字符串
s = b'hello world'
b = s.decode('utf-8')

# 将一个整数转换为有符号的字符
n = -37
m = ctypes.c_byte(n).value

# 将一个整数转换为有符号的字符
n = -37
