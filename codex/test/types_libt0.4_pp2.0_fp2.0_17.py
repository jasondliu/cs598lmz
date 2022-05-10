import types
types.FunctionType

# 判断是否是某种类型
isinstance(abs, types.BuiltinFunctionType)

# 获取一个对象的所有属性和方法
dir('ABC')

len('ABC')
'ABC'.__len__()

# 获取属性
getattr(obj, 'x')
# 设置属性
setattr(obj, 'y', 19)
# 判断是否有属性
hasattr(obj, 'y')
# 删除属性
delattr(obj, 'y')

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# 使用@property
