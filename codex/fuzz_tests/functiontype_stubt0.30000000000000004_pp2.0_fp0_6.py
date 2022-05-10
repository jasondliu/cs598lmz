from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def f():
    yield 1

print(isinstance(f(), GeneratorType))
print(isinstance(f(), FunctionType))

# 判断是否是可调用对象
from collections import Iterable
print(callable(f))
print(callable(a))
print(callable(isinstance))
print(callable(Iterable))

# 判断是否是可迭代对象
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance(123, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))
