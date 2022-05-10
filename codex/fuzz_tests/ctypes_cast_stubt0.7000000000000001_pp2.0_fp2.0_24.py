import ctypes
ctypes.cast(0, ctypes.py_object).value

# 检查一个对象是不是None
ctypes.cast(None, ctypes.py_object).value is None

# 检查一个对象是不是真
ctypes.cast(True, ctypes.py_object).value

# 检查一个对象是不是假
ctypes.cast(False, ctypes.py_object).value

# 检查一个对象是不是一个整数
ctypes.cast(123, ctypes.py_object).value

# 检查一个对象是不是一个浮点数
ctypes.cast(123.45, ctypes.py_object).value

# 检查一个对象是不是一个字节串
ctypes.cast(b"
