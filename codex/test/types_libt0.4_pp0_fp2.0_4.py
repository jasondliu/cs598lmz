import types
types.MethodType(f, None, Student)

# 使用__slots__限制对实例属性的绑定
class Student(object):
    __slots__ = ('name', 'age')

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
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
s.score

# 多重继承
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass
