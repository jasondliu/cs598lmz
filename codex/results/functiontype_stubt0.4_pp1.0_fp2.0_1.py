from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))

print(type(lambda x: x) == FunctionType)
print(type(lambda x: x) == types.FunctionType)
print(type(lambda x: x) == types.LambdaType)

print(type(lambda x: x) == types.GeneratorType)

print(type(lambda x: x) == types.CodeType)
print(type(lambda x: x).__code__ == types.CodeType)

print(type(lambda x: x) == types.MethodType)
print(type(lambda x: x).__call__ == types.MethodType)

print(type(lambda x: x) == types.BuiltinFunctionType)
print(type(lambda x: x).__call__ == types.BuiltinFunctionType)

print(type(lambda x: x) == types.BuiltinMethodType)
print(type(lambda x: x).__call__ == types.BuiltinMethodType)

print(type(lambda x: x) == types.ModuleType)
print
