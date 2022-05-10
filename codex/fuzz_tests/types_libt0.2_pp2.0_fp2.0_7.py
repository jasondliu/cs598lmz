import types
types.FunctionType

# 判断是否是函数
def fn():
    pass

print(type(fn) == types.FunctionType)

# 判断是否是类
class Dog(object):
    pass

print(type(Dog) == types.ClassType)

# 判断是否是模块
import types
print(type(types) == types.ModuleType)

# 判断是否是字符串
print(type('abc') == types.StringType)

# 判断是否是Unicode字符串
print(type(u'abc') == types.UnicodeType)

# 判断是否是整数
print(type(1) == types.IntType)

# 判断是否是浮点数
print(type(1.0) == types.FloatType)

# 判断是
