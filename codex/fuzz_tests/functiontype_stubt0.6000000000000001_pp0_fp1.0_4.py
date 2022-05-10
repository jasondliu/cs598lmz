from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(type(FunctionType))

# 判断一个对象是否是函数
import types
def fn():
    pass
print(type(fn) == types.FunctionType)

# 判断一个对象是否是generator
import types
print(type(fn) == types.GeneratorType)

# 判断一个对象是否是Iterable
from collections import Iterable
print(isinstance([],Iterable))

# 判断一个对象是否是Iterator
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))

# 将Iterable变成Iterator
print(isinstance(iter([]),Iterator))

# 你的代码中有任何的for...in循环，都可以通过next
