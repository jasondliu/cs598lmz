import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 使用__slots__
# 在Python中，每个实例都有__dict__属性，用来存储实例变量。
# 如果你不需要使用实例变量，可以把__slots__定义为空元组，这样就不会有__dict__了。
# 定义__slots__后，只允许实例添加指定的属性。
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# 使用@
