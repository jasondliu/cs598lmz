from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab', 2.7)

# 给类属性添加装饰器
class MyObject:
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

hasattr(obj, 'x')
hasattr(obj, 'y')
setattr(obj, 'y', 19)
hasattr(obj, 'y')
getattr(obj, 'y')
obj.y

getattr(obj, 'z', 404)

class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)

s = Student()
s.score = 90

