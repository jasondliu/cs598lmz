import types
types.MethodType(func, obj)

# 使用__slots__
# 只允许对Student实例添加name和age属性
class Student(object):
    __slots__ = ('name', 'age')

# 使用@property
# 只允许对Student实例添加score属性
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
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass


