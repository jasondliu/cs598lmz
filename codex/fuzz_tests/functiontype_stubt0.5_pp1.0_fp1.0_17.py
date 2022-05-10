from types import FunctionType
a = (x for x in [1])
print(type(a))

def f():
    pass

print(type(f))
print(type(FunctionType))

print(type(f) == FunctionType)
print(isinstance(f, FunctionType))

print(type(f()))
