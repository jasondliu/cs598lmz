import ctypes
ctypes.cast('hello', ctypes.py_object).value

# 如果没有底层C代码支持这种转换，你可以使用ctypes模块中的c_char_p类型来表示一个字符串：
import ctypes
s = b'hello world'
c_s = ctypes.c_char_p(s)
c_s
c_s.value

# 与其他编程语言不同的是，Python不会强制你去声明变量的类型。 因此，你可以把任何东西赋值给变量，同时任何变量可
