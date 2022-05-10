from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == FunctionType)
print(type(b) == FunctionType)
print(type(a) is FunctionType)
print(type(b) is FunctionType)

def f():
    yield 1

print(type(f()) == type(a))
print(type(f()) is type(a))
print(type(f()) == type(b))
print(type(f()) is type(b))
print(type(f()) == FunctionType)
print(type(f()) is FunctionType)

print(type(f) == type(a))
print(type(f) is type(a))
print(type(f) == type(b))
print(type(f) is type(b))
print(type(f) == FunctionType)
print(type(f) is
