from types import FunctionType
a = (x for x in [1])
print(type(a))

def a():
    pass
print(type(a))
print(type(a) == FunctionType)

print(type(a) == type(lambda x:x))

print(type(a) == type(int))

print(type(a) == type(123))

print(type(a) == type(123.4))

print(type(a) == type('abc'))

print(type(a) == type([]))

print(type(a) == type(()))

print(type(a) == type({}))

print(type(a) == type(set()))

print(type(a) == type(frozenset()))

print(type(a) == type(True))

print(type(a) == type(None))

print(type(a) == type(Ellipsis))

print(type(a) == type(NotImplemented))

print(type(a) == type(range(1)))

print(type(a) ==
