from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x: x for x in [1]}
e = FunctionType(lambda x: x, globals())

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(isinstance(d, GeneratorType))
print(isinstance(e, GeneratorType))

print(isinstance(a, list))
print(isinstance(b, list))
print(isinstance(c, list))
print(isinstance(d, list))
print(isinstance(e, list))

print(isinstance(a, dict))
print(isinstance(b, dict))
print(isinstance(c, dict))
print(isinstance(d, dict))
print(isinstance(e, dict))

print(isinstance(a, set))

