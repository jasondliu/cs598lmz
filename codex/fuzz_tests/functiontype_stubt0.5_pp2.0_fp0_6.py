from types import FunctionType
a = (x for x in [1])
b = lambda x: x
c = FunctionType(lambda x: x, globals())

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))

print(isinstance(a, list))
print(isinstance(b, list))
print(isinstance(c, list))

print(isinstance(a, tuple))
print(isinstance(b, tuple))
print(isinstance(c, tuple))

print(isinstance(a, dict))
print(isinstance(b, dict))
print(isinstance(c, dict))

print(isinstance(a, set))
print(isinstance(b, set))
print(isinstance(c, set))

print(isinstance(a, object))
print(isinstance(b, object))
print(isinstance(c, object))

print(isinstance(a, str))
