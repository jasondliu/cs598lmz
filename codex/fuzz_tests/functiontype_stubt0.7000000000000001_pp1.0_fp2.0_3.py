from types import FunctionType
a = (x for x in [1])
print(type(a))

a = map(lambda x: x, a)
print(type(a))

a = list(a)
print(type(a))

a = FunctionType(a, None, None, None, None)
print(type(a))

a = a()
print(type(a))

a = list(a)
print(type(a))

a = dict(a)
print(type(a))

a = set(a)
print(type(a))

a = frozenset(a)
print(type(a))

a = bytes(a)
print(type(a))

a = bytearray(a)
print(type(a))

a = memoryview(a)
print(type(a))

a = tuple(a)
print(type(a))

a = dict(a)
print(type(a))

a = set(a)
print(type(a))

a = frozenset(a)
print(type(a))

a
