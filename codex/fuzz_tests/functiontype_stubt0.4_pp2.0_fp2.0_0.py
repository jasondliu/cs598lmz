from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(isinstance(abs, FunctionType))

print(isinstance(abs, (FunctionType, BuiltinFunctionType)))
print(isinstance(a, (FunctionType, BuiltinFunctionType)))

print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
