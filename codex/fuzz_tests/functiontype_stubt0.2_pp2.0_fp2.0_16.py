from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 判断是否是可迭代对象
from collections import Iterable
print(isinstance(a, Iterable))

# 判断是否是迭代器
from collections import Iterator
print(isinstance(a, Iterator))

# 将可迭代对象转换为迭代器
b = iter(a)
print(isinstance(b, Iterator))

# 将迭代器转换为列表
c = list(b)
print(c)

# 将迭代器转换为元组
d = tuple(b)
print(d)

# 将迭代器转换为集合
e = set(b)
