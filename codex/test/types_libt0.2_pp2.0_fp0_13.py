import types
types.MethodType(func, None, class_name)

# 为实例绑定属性
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age

# 为类绑定属性
class_name.set_score = MethodType(set_score, class_name)
s.set_score(100)
s.score

# 使用__slots__
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

