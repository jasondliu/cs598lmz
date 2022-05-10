import ctypes
ctypes.cast(5, ctypes.py_object)

# py_object isn't a type

# ctypes.cast(5, ctypes.py_object).value

# 使用ctypes进行类型转换，将Python对象强制转换为C类型
ctypes.cast(obj, type)
 
# 使用ctypes.py_object将C类型转换为Python对象
ctypes.py_object

# ctypes模块的内置类型(字符串)

# c_char
# c_wchar
# c_byte
# c_ubyte
# c_short
# c_ushort
# c_int
# c_uint
# c_long
# c_ulong
# c_longlong
# c_ulonglong
# c_float
# c_double
