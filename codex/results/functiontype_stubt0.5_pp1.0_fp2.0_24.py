from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])

def test(x):
    pass

print(isinstance(test, FunctionType))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

print(type(test))
print(type(a))
print(type(b))

print(type(a) == type(b))
