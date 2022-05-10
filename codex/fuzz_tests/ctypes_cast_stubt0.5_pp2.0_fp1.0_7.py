import ctypes
ctypes.cast(0, ctypes.py_object).value

# 检查对象是否有给定的属性
hasattr(obj, 'x')  # 有属性'x'吗？

# 获取对象属性
getattr(obj, 'y')  # 获取属性'y'

# 设置对象属性
setattr(obj, 'z', 19)  # 设置属性'z'

# 获取对象方法
hasattr(obj, 'power')  # 有属性'power'吗？

# 获取对象方法
getattr(obj, 'power')  # 获取属性'power'
