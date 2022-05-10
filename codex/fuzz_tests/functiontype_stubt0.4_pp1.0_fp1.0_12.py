from types import FunctionType
a = (x for x in [1])
print(type(a))
print(a)
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

# 判断是否可迭代
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

# 判断是否是生成器
from types import GeneratorType
print(isinstance((x for x in range(10)), GeneratorType))
print(isinstance
