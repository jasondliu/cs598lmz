import types
types.MethodType

class Student(object):
    pass

def set_age(self,age): # 定义一个函数作为实例方法
    self.age = age

s = Student()
s.name = 'Michael' # 给实例绑定一个属性
print(s.name)

from types import MethodType
s.set_age = MethodType(set_age,s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) # 测试结果

s2 = Student() # 创建新的实例
s2.set_age(30)

def set_score(self,score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print
