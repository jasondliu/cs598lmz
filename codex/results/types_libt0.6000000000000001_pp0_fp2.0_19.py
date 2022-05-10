import types
types.MethodType(f, None, Student)

# __slots__ 动态语言的限制
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

#使用@property

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

class Screen(object):

    @property
    def width(self):
        return
