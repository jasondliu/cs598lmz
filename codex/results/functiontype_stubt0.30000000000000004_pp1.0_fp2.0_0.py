from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(a)
print(b)
print(type(a))
print(type(b))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

# 以下代码可以看出，生成器是一个迭代器，但是迭代器不一定是生成器
from collections import Iterator
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))

# 列表生成式
print([x for x in range(10)])
print([x for x in range(10) if x % 2 == 0])
print([x for x in range(10) if x % 2 == 0 if x % 3 == 0])
print([x + y for x in range(10) if x % 2 == 0 for y in range(10) if
