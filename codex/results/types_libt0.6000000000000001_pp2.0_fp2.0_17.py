import types
types.MethodType(f,None,Hello)

print(hello.name)

# 给实例绑定一个属性
hello.name = 'Michael'
print(hello.name)
# 给实例绑定一个方法
def set_age(self,age):
    self.age = age
from types import MethodType
hello.set_age = MethodType(set_age,hello)
hello.set_age(25)
print(hello.age)

# 使用__slots__限制实例的属性
class Student(object):
    __slots__ = ('name','age') # 用tuple定义允许绑定的属性名称
s = Student()
s.name = 'Michael'
s.age = 25
print(s.name,s.age)
# s.score = 99 # 绑定属
