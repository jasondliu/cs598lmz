import ctypes
ctypes.cast(0, ctypes.py_object).value

# 如果一个C函数返回一个指针，那么你可以使用 restype 参数来指定返回值类型。
# 下面是一个简单的C函数，返回一个指向一个字符串的指针：

import ctypes
libc = ctypes.CDLL(None)
c_strchr = libc.strchr
c_strchr.argtypes = (ctypes.c_char_p, ctypes.c_int)
c_strchr.restype = ctypes.c_char_p

# 如果一个C函数返回一个指针，那
