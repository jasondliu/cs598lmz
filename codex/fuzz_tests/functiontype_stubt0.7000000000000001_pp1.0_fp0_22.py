from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(type(a), type(b), type(a) == type(b))

print(type(lambda x: x), type(lambda x: x) == type(lambda y: y))
print(type(lambda x: x) == FunctionType)
