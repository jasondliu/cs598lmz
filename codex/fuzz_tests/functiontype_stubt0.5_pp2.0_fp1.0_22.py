from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)

# 判断是否为可调用对象
print(callable(a))
print(callable(FunctionType))
print(callable(lambda x: x))

# 判断是否为迭代器
from collections import Iterator
print(isinstance(a, Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# 判断是否为可迭代对象
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))

# 判断是否为生成器
print(isinstance((x for x in range(10)), Iterator))
print(isinstance((x for x in range(10)), Iterable))
print(is
