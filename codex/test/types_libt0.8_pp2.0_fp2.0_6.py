import types
types.MethodType(f, None, Student)

# __slots__ : 用来限制对对象绑定的属性
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称, 对继承自Student的子类是不起作用的
