from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)

b = (x for x in [1])
print(type(b))
print(type(b) == GeneratorType)

print(a == b)

c = (x for x in [1])
print(type(c))
print(type(c) == GeneratorType)

print(a == c)

d = (x for x in [1])
print(type(d))
print(type(d) == GeneratorType)

print(a == d)

print(a is b)
print(a is c)
print(a is d)

print(a == b)
print(a == c)
print(a == d)

print(a == a)
print(a is a)

print(b == b)
print(b is b)

print(c == c)
print(c is c)

print(d == d)
print(d is d)

print(a == b)
print(a == c)
print(a
