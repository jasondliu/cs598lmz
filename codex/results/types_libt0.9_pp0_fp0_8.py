import types
types.MethodType

#part 2
import types
class Student():
    def __init__(self):
        self.name = '小明'
        self.score = 0
    def do_homework(self):
        print('homework')
    def __str__(self):
        return 'str函数内容'
    __repr__ = __str__
 

student1 = Student()
print(student1.__dict__)
print(student1)
student1.__dict__['gender'] = '男'
print(student1.gender)
student1.score = 100
print(student1.score)

def set_age(self,age):
    self.age = age

from types import MethodType
student1.set_age = MethodType(set_age,student1)
student1.set_age(25)
print(student1.age)

#part 3
class Student():
    pass

s = Student()
s.score = 9
print(s.score)

#part 4
class Student
