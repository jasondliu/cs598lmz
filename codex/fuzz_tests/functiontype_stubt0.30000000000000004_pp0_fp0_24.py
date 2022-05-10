from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 判断是否可迭代
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 判断是否为数字
from collections import Iterable
print(isinstance(100, Iterable))
print(isinstance(100, Iterable))
print(isinstance(100, Iterable))
print(isinstance(100, Iterable))
print(isinstance(100, Iterable))

# 判断是否为数字
from collections import Iterable
print(isinstance(100, Iterable))
print(isinstance(100, Iterable))
print(isinstance(100, Iterable))
print(isinstance(100, Iterable))
