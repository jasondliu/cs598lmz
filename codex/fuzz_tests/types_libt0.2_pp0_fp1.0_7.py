import types
types.MethodType(f, None, Student)

# 为实例绑定一个方法
s.set_age = MethodType(f, s)
s.set_age(25)
s.age

# 为类绑定方法
Student.set_score = MethodType(f, None, Student)
s.set_score(100)
s.score

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25
s.score = 99

# 使用@property
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError
