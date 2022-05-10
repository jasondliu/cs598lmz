from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(type(a) == type(b))
print(a is b)

print(type(a) == FunctionType)
print(type(a) == GeneratorType)

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

# 将可迭代对象转换为迭代器
print(isinstance(iter([]), Iterator))
