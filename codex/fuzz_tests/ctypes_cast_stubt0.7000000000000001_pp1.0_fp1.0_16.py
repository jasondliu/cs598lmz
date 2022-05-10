import ctypes
ctypes.cast(1, ctypes.py_object)

# 除数取余
ctypes.cast(1, ctypes.c_char)

# 数据类型转换数组
print (ctypes.cast(1, ctypes.c_char * 2))

# 数据类型转换指针
ctypes.cast(1, ctypes.POINTER(ctypes.c_char))

# 数据类型转换指针数组
ctypes.cast(1, ctypes.POINTER(ctypes.c_char * 2))

# 数据类型转换指针
ctypes.cast(1, ctypes.POINTER(ctypes.c_char * 2))
ctypes.cast(1, ctypes.POINTER(ctypes.POINTER(ct
