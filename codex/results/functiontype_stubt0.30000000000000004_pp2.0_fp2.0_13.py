from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(type(a))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))
print(isinstance(a, type(b)))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, list))
print(isinstance(a, tuple))
print(isinstance(a, set))
print(isinstance(a, dict))

# print(isinstance(a, int))

# print(isinstance(a, str))

# print(isinstance(a, float))

# print(isinstance(a, complex))

# print(isinstance(a, bool))

# print(isinstance(a, bytes))

# print(isinstance(a, bytearray))

# print(isinstance(a, memoryview))

# print(isinstance(a, range))

# print(isinstance(a, slice))

# print(isinstance(a,
