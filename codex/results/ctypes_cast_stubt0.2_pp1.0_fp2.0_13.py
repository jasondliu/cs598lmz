import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 判断一个对象是否是另一个类型的实例
isinstance(obj, int)

# 判断一个对象是否是另一个类型本身
type(obj) is type

# 判断一个对象是否是另一个类型的子类
issubclass(bool, int)

# 获得一个对象的所有属性和方法
dir('ABC')

# 类似 __xxx__ 的属性和方法在 Python 中都是有特殊用途的，比如 __len__ 方法返回长度。
#
