import types
types.MethodType(rank, dog)

# 关于给实例绑定方法的两种写法，上面的是最简单的写法，还有一种写法，如下：
def set_age(self, age):
    self.age = age

from types import MethodType
dog.set_age = MethodType(set_age, dog)
dog.set_age(23)
dog.age

# 另外第三种是使用@property装饰器，如下：
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise
