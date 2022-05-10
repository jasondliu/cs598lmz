import types
types.MethodType(f, None, class_name)

# 测试:
class Student(object):
    pass
s = Student()
s.name = 'Michael'
print(s.name)
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) # 测试结果

# 给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student() # 创建新的实例
#s2.set_age(25
