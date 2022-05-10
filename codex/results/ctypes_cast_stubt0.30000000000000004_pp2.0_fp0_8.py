import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes.cast()将整型转换为指针
int_p = ctypes.cast(0, ctypes.POINTER(ctypes.c_int))
int_p.contents.value

# 使用ctypes.cast()将指针转换为整型
ctypes.cast(int_p, ctypes.c_void_p).value

# 使用ctypes.cast()将指针转换为Python对象
ctypes.cast(int_p, ctypes.py_object).value

# 使用ctypes.cast()将Python对象转换为指针
ctypes.cast(ctypes.py_object(42), ctypes.POINTER(ctypes.c_int))

# 使用ctypes.cast()将指
