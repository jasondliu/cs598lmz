from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])

print(a)
print(b)
print(a == b)
print(a is b)

print("\n")

print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))

print("\n")

print(FunctionType)
print(type(a))
print(FunctionType == type(a))
print(FunctionType is type(a))

print("\n")

print(dir(a))
print(dir(b))
print(dir(a) == dir(b))
print(dir(a) is dir(b))

print("\n")

print(id(a))
print(id(b))
print(id(a) == id(b))
print(id(a) is id(b))

print("\n")

print(hash(a))
print(hash(b))
print(hash(a) == hash(b))
print(hash(a
