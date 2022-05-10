import types
types.MethodType

class Student(object):
    pass

s = Student()
# 动态给实例绑定一个属性
s.name = 'Michael'
