from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

b = FunctionType(a)
print(b(1))
