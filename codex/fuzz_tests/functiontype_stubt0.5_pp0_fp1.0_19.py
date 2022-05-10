from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 判断一个对象是否是可调用对象
from types import FunctionType

def f():
    pass

print(isinstance(f, FunctionType))
print(isinstance(f, FunctionType))

# 判断一个对象是否是模块
import sys
print(isinstance(sys, ModuleType))

# 判断一个对象是否是类型或者函数
from types import FunctionType
def f():
    pass
print(isinstance(f, FunctionType))
print(isinstance(f, FunctionType))

# 判断一个对象是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print
