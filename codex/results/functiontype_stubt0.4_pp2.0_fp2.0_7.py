from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(type(FunctionType))

# 判断一个对象是否是函数
print(callable(print))
print(callable(lambda x: x))
print(callable(lambda x, y: x + y))

# 判断一个对象是否是可迭代对象
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 判断一个对象是否是迭代器
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
