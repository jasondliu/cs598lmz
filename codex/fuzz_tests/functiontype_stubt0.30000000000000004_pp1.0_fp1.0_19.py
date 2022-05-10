from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 判断一个对象是否是函数
from types import FunctionType
def fn():
    pass

print(type(fn) == FunctionType)
print(isinstance(fn, FunctionType))

# 判断一个对象是否是模块
from types import ModuleType
import sys
print(type(sys) == ModuleType)
print(isinstance(sys, ModuleType))

# 判断一个对象是否是类型
from types import TypeType
print(type(int) == TypeType)
print(isinstance(int, TypeType))

# 判断一个对象是否是布尔类型
from types import BooleanType
print(type(True) == BooleanType)
print(isinstance(True,
