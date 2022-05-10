from types import FunctionType
a = (x for x in [1])

b = (x for x in [1])

assert isinstance(a, GeneratorType)
print(type(a))
print(a)

assert isinstance(b, GeneratorType)
print(type(b))
print(b)

assert a != b
