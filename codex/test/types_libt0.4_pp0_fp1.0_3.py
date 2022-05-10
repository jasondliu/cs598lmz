import types
types.MethodType(func, obj)

# 为实例绑定的方法，只对当前实例起作用，对其他实例无效
class Student(object):
    pass

s = Student()
s.name = 'Michael'

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
s.age # 测试结果

s2 = Student() # 创建新的实例
s2.set_age(25) # 尝试调
