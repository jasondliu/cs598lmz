from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

b = (x for x in [1])
print(b)
print(type(b))

print(a == b)

c = (x for x in [1])
print(c)
print(type(c))

print(a == c)

def func():
    yield 1

d = func()
print(d)
print(type(d))

print(a == d)

e = func()
print(e)
print(type(e))

print(d == e)

f = func()
print(f)
print(type(f))

print(d == f)

print(isinstance(func, FunctionType))
print(isinstance(d, FunctionType))
