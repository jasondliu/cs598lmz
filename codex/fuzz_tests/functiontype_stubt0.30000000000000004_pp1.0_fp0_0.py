from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.FunctionType)
print(type(a.__next__) == types.BuiltinFunctionType)
print(type(a.__next__) == types.MethodType)
print(type(a.__next__) == types.BuiltinMethodType)

print(dir(a))
print(dir(a.__next__))
print(dir(a.__next__.__code__))
print(dir(a.__next__.__code__.co_code))
print(dir(a.__next__.__code__.co_code.__class__))
print(dir(a.__next__.__code__.co_code.__class__.__base__))
print(dir(a.__next__.__code__.co_code.__class__.__base__.__base__))
print(dir(a.__next__.__code__.co
