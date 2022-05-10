import types
types.MethodType(c, obj)
class Student:
    pass
def set_age(self, age):
    self.age = age
def set_score(self, score):
    self.score = score

s = Student()
s.name = 'Michael'

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_score = MethodType(set_score, s)

s.set_age(25)
s.set_score(100)
print(s.age)
print(s.score)
class Student:
    pass

# s = Student()
# s.name = 'Michael' # 动态给实例绑定一个属性
# print(s.name)
#
# def set_age(self, age): # 定义一个函数作为实例方法
#     self.age = age
#
# from types import MethodType
# s.set_age = Method
