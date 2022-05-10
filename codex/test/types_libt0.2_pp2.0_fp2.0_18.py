import types
types.MethodType(f, None, Student)

# 为实例绑定属性
s.name = 'Michael'
print(s.name)

# 为实例绑定方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
# s2.set_age(25)

# 为所有实例绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)

s
