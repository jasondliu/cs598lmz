from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, list))

# 判断是否是可迭代对象
from collections import Iterable
print(isinstance(a, Iterable))

# 判断是否是迭代器
from collections import Iterator
print(isinstance(a, Iterator))

# 判断是否是生成器
from types import GeneratorType
print(isinstance(a, GeneratorType))

# 判断是否是函数
from types import FunctionType
print(isinstance(a, FunctionType))

# 判断是否是列表
print(isinstance(a, list))
