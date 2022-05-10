import types
types.MethodType(f, None, Student)

# 使用__slots__
# 在定义类的时候，可以使用__slots__来限制类的实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99 这个是错误的

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
