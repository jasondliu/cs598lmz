import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 把一个对象的内存地址转化为一个整数
ctypes.cast(id(obj), ctypes.c_void_p).value

# 把一个整数转换为一个对象
ctypes.cast(ctypes.c_void_p(id(obj)), ctypes.py_object).value

# 把一个整数转换为一个对象
ctypes.cast(ctypes.c_ulong(id(obj)), ctypes.py_object).value
