import types
types.MethodType(f, None, class_name)

# 为实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25)
s.age

# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
s2.set_age(25) # AttributeError: 'Student' object has no attribute 'set_age'

# 为所有实例绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
s.score

s2.
