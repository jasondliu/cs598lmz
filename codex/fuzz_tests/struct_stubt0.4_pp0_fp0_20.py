from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(1)

# 创建一个类，没有继承关系，但是还是可以使用其他类的方法
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

s = Student('Bob')
s.score = 90
print(s.score)

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999

# 使用@property
class Student(object):
    @property
    def score(self):
        return
