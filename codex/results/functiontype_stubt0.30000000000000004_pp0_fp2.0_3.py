from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))
print(type(abs))
print(type(a) == type(lambda x: x))
print(type(a) == FunctionType)
print(type(a) == types.GeneratorType)

# 判断一个对象是否是函数
import types

def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 判断一个对象是否是可调用对象
import types

def fn():
    pass

print(callable(fn))
print(callable(abs))
print(callable(lambda x: x))
print(callable
