from types import FunctionType
a = (x for x in [1])
print(type(a))
print(a is iter([1]))

print(iter([1]))
print(len([1]))

def func(a, b):
    return a + b

print(type(func))
print(isinstance(func, F
