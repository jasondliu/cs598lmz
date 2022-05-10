from types import FunctionType
a = (x for x in [1])
print(type(a))

b = lambda x: x
print(type(b))
print(type(FunctionType))

def fn(x):
    return x

print(type(fn))
