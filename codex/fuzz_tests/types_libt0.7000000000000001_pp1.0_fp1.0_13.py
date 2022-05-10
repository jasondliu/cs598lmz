import types
types.FunctionType

# staticmethod
# staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。

#使用@staticmethod或@classmethod，就可以不用定义类，就可以这样做
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
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth
