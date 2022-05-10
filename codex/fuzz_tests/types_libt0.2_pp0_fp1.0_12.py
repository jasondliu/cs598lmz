import types
types.MethodType(f, None, class_name)

# 为实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age

# 为所有实例绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
s.score

s2.set_score(99)
s2.score

# 限制实例的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age =
