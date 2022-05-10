from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__iter__()) == a)
print(type(a.__next__))
print(type(a.__next__()) == int)

def b():
    yield 1
print(type(b))
print(type(b()) == FunctionType)
print(type(b().__iter__))
print(type(b().__iter__()) == b)
print(type(b().__next__))
print(type(b().__next__()) == int)

print(b() == b())
print(b().__iter__() == b().__iter__())

# 可迭代对象
from collections import Iterable
print(isinstance((x for x in range(10)), Iterable))
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))
