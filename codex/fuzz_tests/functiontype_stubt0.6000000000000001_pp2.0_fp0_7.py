from types import FunctionType
a = (x for x in [1])
b = (y for y in [2])
print(type(a))
print(type(b))

def c(x):
    return x

print(isinstance(c, FunctionType))

def d():
    return

print(isinstance(d, FunctionType))

def e():
    return 1

print(isinstance(e, FunctionType))
