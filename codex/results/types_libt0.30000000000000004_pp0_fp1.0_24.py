import types
types.MethodType(foo, obj)

# 关于__slots__
# 用tuple定义允许绑定的属性名称
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999

# 使用@property
# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身
