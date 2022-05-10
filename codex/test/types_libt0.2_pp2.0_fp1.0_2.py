import types
types.FunctionType

# 判断是否是函数
def fn():
    pass

print(type(fn) == types.FunctionType)

# 判断是否是类
class Animal(object):
    pass

print(type(Animal) == types.ClassType)

# 判断是否是模块
import sys
print(type(sys) == types.ModuleType)

# 判断是否是字符串
print(type('abc') == types.StringType)

# 判断是否是整数
print(type(1) == types.IntType)

# 判断是否是浮点数
print(type(1.2) == types.FloatType)

# 判断是否是布尔值
print(type(True) == types.BooleanType)

# 判断是否是复数
