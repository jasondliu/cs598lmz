from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

print(type(abs) == FunctionType)
print(type(abs) == GeneratorType)

print(type(lambda x: x) == FunctionType)
print(type(lambda x: x) == GeneratorType)

print(type(x for x in range(10)) == FunctionType)
print(type(x for x in range(10)) == GeneratorType)

print(type((lambda x: x)) == FunctionType)
print(type((lambda x: x)) == GeneratorType)

print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

print(isinstance(abs, FunctionType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance(lambda x: x, types.LambdaType))
print(isinstance(x for x in range(
