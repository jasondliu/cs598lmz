from types import FunctionType
a = (x for x in [1])
b = (y for y in [1])
c = (z for z in [1])
d = [a, b, c]
e = [d, d]

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(isinstance(d, list))
print(isinstance(e, list))

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(type(e) == list)
print(type(eval('e')) == list)

print(type(e) == list == True)
print(isinstance(e, list) == True)

print(isinstance(a, GeneratorType) == True)
print(isinstance(b, GeneratorType) == True)
print(isinstance(c, GeneratorType) == True)
print(isinstance(d, list) == True)
print(isinstance(e, list) == True)

print(isinstance
