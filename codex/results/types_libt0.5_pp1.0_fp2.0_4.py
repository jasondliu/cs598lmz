import types
types.MethodType

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Bob', 30)
p.name

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
p.set_age = MethodType(set_age, p) # 给实例绑定一个方法
p.set_age(25) # 调用实例方法
p.age # 测试结果

def set_score(self, score):
    self.score = score

Person.set_score = set_score # 给class绑定方法

p.set_score(100)
p.score

p2 = Person('Jack', 20)
p2.set_score(90)
p2.score

