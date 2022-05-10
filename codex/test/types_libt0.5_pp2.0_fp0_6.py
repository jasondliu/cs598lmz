import types
types.MethodType(f, None, class_name)

# 给一个实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)

# 给所有实例都绑定方法
def set_score(self, score):
    self.score = score

class_name.set_score = MethodType(set_score, class_name)

s.set_score(100)
s2.set_score(99)

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25

# @property

