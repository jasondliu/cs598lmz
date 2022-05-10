from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 迭代器
from collections import Iterable
from collections import Iterator
a = [1, 2, 3]
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

# 可迭代对象
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#
