from types import FunctionType
a = (x for x in [1])
print a

def f():
    pass

print isinstance(f, FunctionType)

def g():
    yield 1

print isinstance(g, FunctionType)
