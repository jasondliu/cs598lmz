from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a==b)
print(type(a))
print(FunctionType)
def foo(x):
    pass

print(type(foo))
