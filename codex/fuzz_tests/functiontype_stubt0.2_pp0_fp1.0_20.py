from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

# 判断一个对象是否是函数
from types import FunctionType
print(type(abs) == FunctionType)

# 判断一个对象是否是生成器函数
from types import GeneratorType
print(type(a) == GeneratorType)

# 判断一个对象是否是迭代器
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# 判断一个对象是否是可迭代对象
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iter
