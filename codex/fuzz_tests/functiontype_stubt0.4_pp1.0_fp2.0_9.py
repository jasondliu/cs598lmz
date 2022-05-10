from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
c = (x for x in [1])

print(a == b)
print(a == c)
print(a is b)
print(a is c)
print(type(a))
print(type(b))
print(type(c))
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))

print(isinstance(a, object))
print(isinstance(b, object))
print(isinstance(c, object))

print(isinstance(a, dict))
print(isinstance(b, dict))
print(isinstance(c, dict))

print(isinstance(a, list))
print(isinstance(b, list))
print(isinstance(c, list))

print(isinstance(a, tuple))
print(isinstance(b, tuple))
print
