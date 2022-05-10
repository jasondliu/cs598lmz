from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

# 判断一个对象是否是可调用对象
from collections.abc import Callable
print(isinstance(a, Callable))

# 判断一个对象是否是可迭代对象
from collections.abc import Iterable
print(isinstance(a, Iterable))

# 判断一个对象是否是迭代器
from collections.abc import Iterator
print(isinstance(a, Iterator))

# 判断一个对象是否是生成器
from collections.abc import Generator
print(isinstance(a, Generator))

# 判断一个对象是否是生成器函数
from collections
