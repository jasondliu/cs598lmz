from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
b = FunctionType
print(isinstance(b, FunctionType))

# 判断一个对象是否是函数
from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))
b = FunctionType
print(isinstance(b, FunctionType))

# 判断一个对象是否是模块
from types import ModuleType
a = (x for x in [1])
print(isinstance(a, ModuleType))
b = FunctionType
print(isinstance(b, ModuleType))

# 判断一个对象是否是类
from types import ModuleType
a = (x for x in [1])
print(isinstance(a, ModuleType))
b = FunctionType
print(isinstance(b, ModuleType))

# 判断一个对象是否是方法
