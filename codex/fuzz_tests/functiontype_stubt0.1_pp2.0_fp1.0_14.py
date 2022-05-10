from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__next__) == type(a.__iter__))
print(type(a.__next__) == FunctionType)
print(type(a.__iter__) == FunctionType)

# 判断是否是可迭代对象
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 判断是否是迭代器
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# 可迭代对象变
