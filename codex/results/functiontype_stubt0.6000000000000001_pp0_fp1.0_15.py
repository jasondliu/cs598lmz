from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(type(a))
print(type(b))
print(type(abs))
print(type(a) == type(b))
print(type(a) == FunctionType)
print(type(abs) == FunctionType)

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(abs, FunctionType))
print(isinstance(abs, GeneratorType))
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

# 迭代器
from collections import Iterable, Iterator
print(isinstance([], Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

# 凡是可作用于for循环
