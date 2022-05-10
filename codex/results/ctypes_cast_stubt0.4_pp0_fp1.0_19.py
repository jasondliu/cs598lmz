import ctypes
ctypes.cast(0, ctypes.py_object).value

# 检查对象是否是一个类型的实例
isinstance(1, int)
isinstance(1.0, int)

# 检查对象是否实现了某个特定的方法
def foo(self, x):
    pass
from types import MethodType
method = MethodType(foo, None, class)
method.__self__
method.__func__
method.__name__

# 检查对象是否是另一个对象的子类
issubclass(bool, int)

# 获取对象的内存地址
id(1)

# 获取对象的类型
type(1)

# 获取对象的
