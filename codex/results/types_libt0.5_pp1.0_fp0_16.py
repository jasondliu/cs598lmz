import types
types.MethodType(f, None, class_)

# 把一个类的所有属性和方法调用全部动态化处理

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

# 动态给实例绑定一个方法

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
s.age # 测试结果

# 给一
