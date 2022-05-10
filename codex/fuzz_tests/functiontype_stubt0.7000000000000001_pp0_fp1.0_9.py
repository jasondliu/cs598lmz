from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))

def a(x):
    return x

print(type(a))

b = a
print(type(b))

def a(x, y):
    return x + y
