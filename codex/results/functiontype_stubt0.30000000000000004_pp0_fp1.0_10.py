from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__()))

print(type(a.__next__) is FunctionType)
print(type(a.__next__()) is int)
print(type(a.__iter__()) is int)

print(type(a.__next__) == FunctionType)
print(type(a.__next__()) == int)
print(type(a.__iter__()) == int)

print(type(a.__next__) is FunctionType)
print(type(a.__next__()) is int)
print(type(a.__iter__()) is int)

print(type(a.__next__) == FunctionType)
print(type(a.__next__()) == int)
print(type(a.__iter__()) == int)

print(type(a.__next__) is FunctionType)
print(type(a.__next__()) is int)
print(type(a.__
