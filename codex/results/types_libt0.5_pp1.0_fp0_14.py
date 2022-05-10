import types
types.MethodType(f, None, class1)

class2.f()

# 给实例绑定一个方法
def set_age(self, age):
    self.age = age

class Student(object):
    pass

s = Student()
s.name = 'Michael'

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age

# 给class绑定方法后，所有实例均可调用
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
s.score

s2 = Student()
s2.set_score(99)
s2.score

# 使用__slots__
# 但是，如果我们想要限
