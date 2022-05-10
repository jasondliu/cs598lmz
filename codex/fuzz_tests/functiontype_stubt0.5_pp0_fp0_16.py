from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in [1])))
print(type(FunctionType))

print("\n")

print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))

print("\n")

print(dir(a))

print("\n")

print(dir(FunctionType))

print("\n")

print(dir(abs))

print("\n")

print(dir(a))

print("\n")

print(dir(lambda x: x))

print("\n")

print(dir(type))

print("\n")

print(dir(object))

print("\n")

print(dir(type))

print("\n")

print(dir(object))

print("\n")

print(dir(object))

print("\n")

print(dir(type))

