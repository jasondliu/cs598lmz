from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

print(isinstance(a, list))
print(isinstance(a, tuple))
print(isinstance(a, set))
print(isinstance(a, dict))

print(isinstance(a, str))
print(isinstance(a, int))
print(isinstance(a, float))

print(isinstance(a, object))
print(isinstance(a, type))

print(isinstance(a, type(None)))

print(isinstance(a, type(lambda x: x)))

print(isinstance(a, type(print)))

print(isinstance(a, type(a)))

print(isinstance(a, type(1)))

print(isinstance(a, type(1.0)))

print(isinstance(a, type('1')))

print(isinstance(a, type([])))

print(isinstance(a
