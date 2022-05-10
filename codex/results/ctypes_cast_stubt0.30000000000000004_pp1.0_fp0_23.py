import ctypes
ctypes.cast(0, ctypes.py_object).value

# 下面的代码会产生一个 TypeError
ctypes.cast("str", ctypes.py_object).value

# 如果需要从一个 C 类型转换到一个 Python 类型，使用 from_param() 方法
ctypes.cast(ctypes.py_object(1), ctypes.c_void_p).value

# 下面的代码会产生一个 TypeError
ctypes.cast(ctypes.py_object("str"), ctypes.c_void_p).value

# 如果需要从一个 C 类型转换到一个 Python 类型，使用 from_param() 方法
ctypes.cast(ctypes.py_object(
