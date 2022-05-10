from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(FunctionType, FunctionType))
print(type(lambda x: x) == types.LambdaType)
print(type(lambda x: x) == types.FunctionType)
print(type(a))
print(type(FunctionType))
