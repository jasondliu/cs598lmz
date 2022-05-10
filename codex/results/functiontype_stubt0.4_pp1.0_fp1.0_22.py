from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)

print(type(a))
print(FunctionType)
print(type(a) == FunctionType)

# 判断一个对象是否是函数
import types
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 使用isinstance()判断一个对象是否是函数
print(isinstance(fn, types.FunctionType))
print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance(lambda x: x, types.LambdaType))
print(isinstance((x for x in range(10)), types.GeneratorType))

# 使用dir()获得一
