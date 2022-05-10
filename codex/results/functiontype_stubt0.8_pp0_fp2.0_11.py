from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a) is type(b))
print((FunctionType, type(lambda x: x))[0] is type(lambda x: x))
print((FunctionType, type(lambda x: x))[1] is type(lambda x: x))

print(type(a) is (FunctionType, type(lambda x: x))[1])
print(type(a) is (FunctionType, type(lambda x: x))[0])

print(type(x for x in []) is FunctionType)
import types
print(type(x for x in []) is types.GeneratorType)
print(type(x for x in []) is types.FunctionType)
