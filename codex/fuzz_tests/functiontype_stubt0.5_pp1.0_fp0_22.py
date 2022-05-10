from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(id(a))
print(id(b))

def f():
    pass

print(type(f))
print(type(FunctionType))
print(type(f) == FunctionType)
