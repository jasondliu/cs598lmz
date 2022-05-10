import types
types.MethodType(f, None, Student)

# 给实例绑定方法
s.set_age(25)
s.age

# 给class绑定方法后，所有实例均可调用
s2 = Student('Bob')
s2.set_age(25)

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
s.score = 99

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score
