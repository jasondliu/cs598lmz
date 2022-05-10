from types import FunctionType
a = (x for x in [1])
print(a)

def f():
    yield 1
print(f)
print(FunctionType)
print(type(f))
