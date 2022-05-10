import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 使用__slots__
# 定义类的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# 使用@property
# 把一个getter方法变成属性，只需要加上@property就可以了
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score
