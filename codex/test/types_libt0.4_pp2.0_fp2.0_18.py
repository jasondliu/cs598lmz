import types
types.MethodType(f, None, class_)

f = types.MethodType(f, None, class_)
f()

class Student(object):
    pass

s = Student()

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
s.age # 测试结果

def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
s.score

s2 = Student()
s2.set_score(99)
s2.score

class Student(object):
    __slots__ = ('name', 'age') #
