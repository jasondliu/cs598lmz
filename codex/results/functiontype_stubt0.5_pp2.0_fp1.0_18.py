from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])

def func():
    yield from a
    yield from b
    yield from c

print(type(func()))
print(type(a))
print(type(b))
print(type(c))

print(type(func) == FunctionType)

for i in func():
    print(i)
