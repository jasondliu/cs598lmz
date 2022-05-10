import types
types.MethodType(f, None, Student)

# 给实例绑定一个方法，只对当前实例起作用
s.set_age = MethodType(f, s)
s.set_age(25)
print(s.age)

# 如果想要限制实例的属性，比如只允许对Student实例添加name和age属性。
# 可以通过在类中定义__slots__变量来进行限制
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

# 使用__slots__要注意
