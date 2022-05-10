import types
types.MethodType(f, None, Dog)

# __slots__
class GraduateStudent(Student):
    pass
s = GraduateStudent()
s.score = 9999

class GraduateStudent(Student):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

g = GraduateStudent()
g.score = 9999

# 使用@property
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
s.score = 60 # OK，实际转化为s.set_score(60)
s.score # OK，
