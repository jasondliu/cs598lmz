from types import FunctionType
a = (x for x in [1])
print(type(a))

b = FunctionType(lambda x: x**2, globals())
print(type(b))

print(type(a) == type(b))

print(type(a) == type(map))

print(type(a) == types.GeneratorType)

print(types.GeneratorType)

print(a == b)

print(map == b)

print(1 == 1.0)

print(type(None))

print(type(NotImplemented))

print(type(Ellipsis))

print(type(0))

print(type(0.0))

print(type(0j))

print(type(True))

print(type(False))
