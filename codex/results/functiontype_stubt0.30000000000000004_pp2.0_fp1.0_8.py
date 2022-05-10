from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.FunctionType)

print(a.__next__())
print(a.__next__())

print(type(a.__iter__) == types.MethodType)
print(type(a.__iter__) == FunctionType)
print(type(a.__iter__) == types.FunctionType)

print(type(a.__iter__()) == types.GeneratorType)
print(type(a.__iter__()) == types.GeneratorType)

print(type(a.__iter__) == FunctionType)
print(type(a.__iter__) == types.FunctionType)

print(type(a.__iter__()) == types.GeneratorType)
print(type(a.__iter__()) == types.GeneratorType)

print(type(a.__iter__) == FunctionType)
print(type(a.__iter__) == types
