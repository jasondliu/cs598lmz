import types
types.MethodType(f, None, Student)

# 为实例绑定属性
s.name = 'Michael'
s.name

# 为实例绑定方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age

# 为类绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
s.score

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
s.score = 99

# 使用@property
class Student(object):

    @property
    def score(self):

