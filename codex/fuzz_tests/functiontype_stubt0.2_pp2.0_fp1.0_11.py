from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in [1])))
print(type(FunctionType))
print(type(FunctionType(lambda x: x, globals())))
print(type(FunctionType(lambda x: x, globals()))())

print(type(FunctionType(lambda x: x, globals())) == FunctionType)
print(type(FunctionType(lambda x: x, globals())) == types.FunctionType)
print(type(FunctionType(lambda x: x, globals())) == types.GeneratorType)
print(type(FunctionType(lambda x: x, globals())) == types.LambdaType)
print(type(FunctionType(lambda x: x, globals())) == types.CodeType)

print(type(abs) == FunctionType)
print(type(abs) == types.FunctionType)
print(type(abs) == types.GeneratorType)
print(type(abs) == types.LambdaType)
print(type
