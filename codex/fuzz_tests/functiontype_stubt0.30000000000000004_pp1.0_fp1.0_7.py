from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, FunctionType))

# 判断一个对象是否是函数
from types import LambdaType
a = lambda x: x
print(type(a))
print(isinstance(a, LambdaType))

# 判断一个对象是否是生成器函数
from types import GeneratorType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))

# 判断一个对象是否是模块
from types import ModuleType
import sys
print(type(sys))
print(isinstance(sys, ModuleType))

# 判断一个对象是否是类型
from types import TypeType
class A:
    pass
print(type(A))
print(isinstance(A, TypeType))

#
