import types
types.MethodType

# 定义一个函数
def set_age(self, age):
    self.age = age

# 创建一个实例
s = Student()

# 给实例绑定一个方法
s.set_age = types.MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 给类绑定方法
Student.set_age = set_age

s2 = Student()
s2.set_age(28)
print(s2.age)

# 使用__slots__
# 限制实例的属性
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

# 使用@property
# 可以
