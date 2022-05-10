import types
types.MethodType(f, None, Student)

# __slots__
# 用tuple定义允许绑定的属性名称
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
