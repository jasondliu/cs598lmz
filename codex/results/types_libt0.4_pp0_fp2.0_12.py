import types
types.MethodType(method, instance)

# __slots__
# __slots__ 的作用是限制实例的属性
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

# @property
# @property 的作用是把一个方法变成属性调用
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

# 多重继承
# 新式类：继承object

