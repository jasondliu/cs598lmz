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
