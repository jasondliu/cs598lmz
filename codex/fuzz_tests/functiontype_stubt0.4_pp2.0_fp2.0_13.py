from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)

print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(a.__next__())
print(a.__next__())

print(b.__next__())
print(b.__next__())

print(a == b)
