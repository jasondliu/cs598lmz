import ctypes
ctypes.cast(0, ctypes.py_object)

# 使用ctypes.cast()函数，可以将一个C类型转换成另一个C类型。
# 下面的例子将一个c_char_p类型转换成一个c_void_p类型：

import ctypes

s = b'Hello World'
s_array = ctypes.c_char_p(s)
print(s_array.value)

s_void_p = ctypes.cast(s_array, ctypes.c_void_p)
print(s_void_p.value)

# 使用ctypes.cast()函数，可以将一个C类型转换成另一个C类型。
# 下
