import types
types.MethodType(f, None, Student)

s = Student()
s.set_age(25)
s.age

# 定义一个函数作为实例方法
def set_score(self, score):
    self.score = score

from types import MethodType
s.set_score = MethodType(set_score, s)
s.set_score(100)
s.score

# 给class绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
s.score

s2 = Student()
s2.set_score(99)
s2.score

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25

s.score = 99

# 使用@property
class Student
