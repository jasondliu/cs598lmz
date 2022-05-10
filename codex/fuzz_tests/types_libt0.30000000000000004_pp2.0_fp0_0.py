import types
types.MethodType(new_func, None, A)

# 使用__slots__
# 定义类的时候，定义一个特殊的__slots__变量，来限制该类能添加的属性
class Student(object):
    __slots__ = ('name', 'age')

# 使用@property
# 定义getter和setter方法，可以对变量进行操作
# 可以通过setter方法来限制变量的范围，可以通过getter方法来获取变量的值
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(
