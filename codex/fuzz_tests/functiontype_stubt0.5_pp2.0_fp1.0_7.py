from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {'x': x for x in [1]}
e = {x: x for x in [1]}
f = FunctionType(lambda x: x, globals())

print(a.__name__)
print(b.__name__)
print(c.__name__)
print(d.__name__)
print(e.__name__)
print(f.__name__)

# __qualname__
def f():
    pass

print(f.__qualname__)

# __slots__
# 可以限制类的属性
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99  # 绑定属性'score'

# __len__
class MyDog(object):
    def __len__(self):

