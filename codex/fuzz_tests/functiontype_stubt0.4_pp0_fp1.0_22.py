from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)
print(type(a) == IteratorType)
print(type(a) == IterableType)

print(type(lambda x: x) == FunctionType)

print(type(abs) == FunctionType)
print(type(abs) == BuiltinFunctionType)
print(type(abs) == MethodType)

print(type(a.__iter__) == BuiltinMethodType)
print(type(a.__next__) == BuiltinMethodType)
print(type(a.__next__) == MethodType)

print(type(a.__iter__) == MethodType)
print(type(a.__iter__) == FunctionType)

print(type(a.__iter__) == MethodType)
print(type(a.__iter__) == FunctionType)

print(type(a.__iter__) == MethodType)
print(type(a.__iter__) == FunctionType)

print(type(a.
