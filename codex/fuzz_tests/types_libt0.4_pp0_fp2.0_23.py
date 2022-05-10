import types
types.MethodType(f, None, class_)

# 使用__slots__
# 在类中定义__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25
s.score = 99

# 使用@property
# 定义一个类的方法，用@property装饰器，就可以把该方法变成属性调用
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(
