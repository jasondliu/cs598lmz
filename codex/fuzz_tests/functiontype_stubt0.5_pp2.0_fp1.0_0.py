from types import FunctionType
a = (x for x in [1])
print(type(a))

b = (x for x in [1])
print(type(b))

print(a == b)

print(type(a) == type(b))

print(type(a) is type(b))

print(FunctionType == type(lambda x: x))

print(type(lambda x: x) == FunctionType)

print(type(lambda x: x) is FunctionType)

print(type(abs))

print(type(abs) == types.BuiltinFunctionType)

print(type(abs) is types.BuiltinFunctionType)

print(type(lambda x: x) == types.LambdaType)

print(type(lambda x: x) is types.LambdaType)

print(type(x for x in range(10)) == types.GeneratorType)

print(type(x for x in range(10)) is types.GeneratorType)

print(isinstance(a, types.GeneratorType))

print(isinstance(a, types.Iterable))


