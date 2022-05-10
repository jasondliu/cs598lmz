import types
types.MethodType(f, None, class_name)

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 99
print(g.score)

# @property
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print(s.score)
# s.score = 999

# 多重继承
class Animal(object):
    pass

class Mammal(Animal):

