from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 使用__slots__
# 只允许添加指定属性
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

# 使用@property
# 把一个getter方法变成属性，只需要加上@property就可以了
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
