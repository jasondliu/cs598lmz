import types
types.FunctionType

# 判断一个对象是否是函数
from types import FunctionType
def fn():
    pass
print(type(fn)==FunctionType)
print(isinstance(fn, FunctionType))
print(type(lambda x: x)==FunctionType)
print(type(abs)==FunctionType)
print(type(int)==FunctionType)

# 判断一个对象是否是生成器函数
from types import GeneratorType
def fn():
    pass
print(type(fn)==GeneratorType)
print(type(abs)==GeneratorType)

# 使用 isinstance()判断一个对象是否是 Iterable 对象
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# 使用 isinstance()判断一
