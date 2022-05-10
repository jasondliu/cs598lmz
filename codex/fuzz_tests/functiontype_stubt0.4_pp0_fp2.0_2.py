from types import FunctionType
a = (x for x in [1])
print(type(a))

b = FunctionType(a)
print(b)

print(type(b))
