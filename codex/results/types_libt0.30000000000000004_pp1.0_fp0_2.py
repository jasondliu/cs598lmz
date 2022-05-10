import types
types.MethodType(f, None, class_name)

# 动态给类绑定方法
def set_age(self, age):
    self.age = age

from types import MethodType
class_name.set_age = MethodType(set_age, class_name)
class_name.set_age(25)
class_name.age

# 给所有实例都绑定方法
class Student(object):
    pass
def set_score(self, score):
    self.score = score

Student.set_score = set_score

stu = Student()
stu.set_score(100)
stu.score

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age')

stu = Student()
stu.name = 'Michael'
stu.age = 25
stu.score = 99

# 使用@property
class Student(object):

   
