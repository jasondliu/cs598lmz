from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, types.GeneratorType))
print(isinstance(a, types.GeneratorType))

# 在循环中，如果判断一个对象是否可以被迭代，则可以使用collections模块的Iterable类型判断
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变
