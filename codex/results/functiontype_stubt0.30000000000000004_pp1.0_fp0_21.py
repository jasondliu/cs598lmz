from types import FunctionType
a = (x for x in [1])
print(type(a))

def a():
    pass

print(type(a))
print(type(a) == FunctionType)
print(type(a) is FunctionType)
print(isinstance(a, FunctionType))
print(isinstance(a, type))
print(isinstance(a, object))
print(isinstance(a, (FunctionType, type)))
print(isinstance(a, (FunctionType, object)))
print(isinstance(a, (FunctionType, int)))
print(isinstance(a, (FunctionType, str)))
print(isinstance(a, (FunctionType, list)))
print(isinstance(a, (FunctionType, tuple)))
print(isinstance(a, (FunctionType, dict)))
print(isinstance(a, (FunctionType, set)))
print(isinstance(a, (FunctionType, frozenset)))
print(isinstance(a, (FunctionType, range)))
print(isinstance(a, (FunctionType, bytes)))
print(isinstance(a, (FunctionType, bytearray)))
print(isinstance(
