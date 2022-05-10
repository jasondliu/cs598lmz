import types
types.MethodType(func, None)

"""
面向对象编程
"""

# 创建类
class Student(object):
    pass

# 创建实例
bart = Student()
print(bart)
print(Student)

# 给实例绑定属性
bart.name = 'Bart Simpson'
print(bart.name)

# 给实例绑定方法
def set_age(self, age):
    self.age = age

from types import MethodType
bart.set_age = MethodType(set_age, bart)
bart.set_age(25)
print(bart.age)

# 可以在创建实例的时候绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

