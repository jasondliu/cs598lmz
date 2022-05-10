from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])

print(a)
print(b)

print(a.__next__())
print(b.__next__())

print(type(a))
print(type(b))

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))


print(a == b)
print(a == a)
print(b == b)

print(id(a))
print(id(b))
print(id(a) == id(b))
print(id(a) == id(a))
print(id(b) == id(b))

print(hash(a))
print(hash(b))
print(hash(a) == hash(b))
print(hash(a) == hash(a))
print(hash(b) == hash(b))

print(a is b)
print(a is a)
print(b is b)

print(a is not
