from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(isinstance(a.__next__, FunctionType))

print(isinstance(lambda x: x, FunctionType))
print(isinstance(lambda x: x, types.FunctionType))
print(isinstance(lambda x: x, types.BuiltinFunctionType))

print(type(lambda x: x))
print(type(types.FunctionType))
print(type(types.FunctionType()) == FunctionType)
print(type(a.__next__) == types.FunctionType)
print(type(a.__next__) == types.BuiltinFunctionType)

print(type(types.FunctionType()) == types.FunctionType)
print(type(types.FunctionType()) == types.BuiltinFunctionType)
