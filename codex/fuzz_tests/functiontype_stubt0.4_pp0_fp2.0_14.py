from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

# 判断是否是可迭代对象
print(hasattr(a, '__iter__'))
print(hasattr(a, '__next__'))
print(hasattr(a, '__getitem__'))

# 判断是否是迭代器
from collections import Iterator
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))

# 判断是否是生成器
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))

# 判断是否是生成器函数
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType
