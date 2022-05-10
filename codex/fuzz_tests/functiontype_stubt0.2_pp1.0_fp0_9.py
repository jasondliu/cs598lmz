from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))

# 判断一个对象是否是可调用对象
from collections import Iterable, Iterator, Generator
from types import FunctionType
a = (x for x in [1])
print(callable(a))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))

# 判断一个对象是否是生成器函数
from collections import Iterable, Iterator, Generator
from types import FunctionType
a = (x for x in [1])
print(isgeneratorfunction(a))
print(isgeneratorfunction(max))
print(isgeneratorfunction([1, 2, 3]))
print(isgenerator
