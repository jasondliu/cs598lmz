from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(isinstance(a, GeneratorType))
print(isinstance(print, FunctionType))

# 判断一个对象是否是函数
import types
def fn():
    pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 判断一个对象是否是可调用对象
from collections import Iterable, Iterator
print(callable(print))
print(callable(a))
print(callable(lambda x: x))
print(callable([]))
print(callable([].__iter__))
print(callable(iter))
print(isinstance([], Iterable))
print(isinstance([], Iterator))
print(is
