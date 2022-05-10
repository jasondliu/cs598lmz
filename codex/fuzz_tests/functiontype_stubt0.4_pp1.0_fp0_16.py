from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(type(abs))
print(isinstance(abs, FunctionType))

# 如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
print(type(lambda x: x))
print(type((x for x in range(10))))
print(type(abs))
print(type(a))

# 使用isinstance()
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, GeneratorType))

# 使用collections模块的Iterable类型判断
from collections import Iterable, Iterator
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(is
