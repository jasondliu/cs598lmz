from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(sum))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in [1])))
print(type(isinstance))

# 判断是否可调用
print(callable(a))
print(callable(sum))
print(callable(abs))
print(callable(lambda x: x))
print(callable((x for x in [1])))
print(callable(isinstance))

# 判断是否是模块
import sys
print(isinstance(sys, ModuleType))

# 判断是否是函数
print(isinstance(abs, FunctionType))

# 判断是否是生成器
print(isinstance((x for x in [1]), GeneratorType))

# 判断是否是类型
print(type(123) == type(456))
print(type
