from types import FunctionType
a = (x for x in [1])
b = {'a': 1}

def c(x):
    return x

print(type(a))
print(type(b))
print(type(c))
print(type(FunctionType))
