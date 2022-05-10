from types import FunctionType
a = (x for x in [1])
print(type(a))
print(a.__next__() == a.next())
a = (x for x in [1, 2, 3])
print(a.__next__())
print(a.__next__())
print(a.__next__())
# print(a.__next__())

print(type(a) == types.GeneratorType)
print(type(a) == types.GeneratorType)
print(type(a) == types.GeneratorType)
print(isinstance(a, types.GeneratorType))
print(isinstance(a, types.GeneratorType))
print(isinstance(a, types.GeneratorType))

print(type(a.__next__))
print(type(a.__next__) == types.BuiltinMethodType)
print(type(a.__next__) == types.BuiltinMethodType)
print(type(a.__next__) == types.BuiltinMethodType)
print(isinstance(a.__next__, types.BuiltinMethodType))
print(isinstance(a.__
