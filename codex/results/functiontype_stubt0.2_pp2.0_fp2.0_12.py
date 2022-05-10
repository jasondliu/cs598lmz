from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in [1])))
print(type(FunctionType))
print(type(FunctionType(lambda x: x, {})))
print(type(FunctionType(lambda x: x, {}))())

print(type(FunctionType(lambda x: x, {})) == FunctionType)
print(type(FunctionType(lambda x: x, {})) == types.FunctionType)
print(type(FunctionType(lambda x: x, {})) == types.GeneratorType)
print(type(FunctionType(lambda x: x, {})) == types.LambdaType)

print(type(FunctionType(lambda x: x, {})) == types.FunctionType)
print(type(FunctionType(lambda x: x, {})) == types.GeneratorType)
print(type(FunctionType(lambda x: x, {})) == types.LambdaType)

print(type(FunctionType(lambda x: x, {})) == types.FunctionType)
print(type
