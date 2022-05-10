from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

print(isinstance(a, list))

print(isinstance(a, tuple))

print(isinstance(a, dict))

print(isinstance(a, set))

print(isinstance(a, frozenset))

print(isinstance(a, str))

print(isinstance(a, bytes))

print(isinstance(a, bytearray))

print(isinstance(a, complex))

print(isinstance(a, float))

print(isinstance(a, int))

print(isinstance(a, bool))

print(isinstance(a, type(None)))

print(isinstance(a, object))

print(isinstance(a, type))

print(isinstance(a, type(type)))

print(isinstance(a, type(object)))

print(isinstance
