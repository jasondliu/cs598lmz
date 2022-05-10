from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

b = (x for x in [1])
print(b)
print(type(b))

print(a == b)
print(id(a) == id(b))

print(type(a) == type(b))

print(a is b)

print(a.__next__())
print(a.__next__())

print(next(b))
print(next(b))

# 判断是否是可迭代对象
from collections import Iterable
print(isinstance(a, Iterable))
print(isinstance(b, Iterable))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))

print(isinstance([], Iterable))
print(isinstance([], Iterator))

print(isinstance(iter([]), Iterable))
print(isinstance(iter([]), Iterator))

print(isinstance(iter([]), Iterable))
print(isinstance(iter([]
