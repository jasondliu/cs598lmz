from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))

# 判断对象是否是函数
print(isinstance(abs, FunctionType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance(a, FunctionType))

# 使用type()判断对象是否是函数
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in [1]) == types.GeneratorType)

# 使用callable()判断对象是否是函数
print(callable(abs))
print(callable(lambda x: x))
print(callable(a))

# 使用isinstance()判断对象是否是函数
print(isinstance(abs, FunctionType))
print(
