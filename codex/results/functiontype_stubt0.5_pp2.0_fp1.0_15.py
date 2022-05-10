from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in range(10))))
print(type(x for x in range(10)))

print(isinstance(a, GeneratorType))
print(isinstance(print, FunctionType))
print(isinstance(abs, FunctionType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance((x for x in range(10)), GeneratorType))
print(isinstance(x for x in range(10), GeneratorType))

# 迭代器
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，
