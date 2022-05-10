from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
print(type(a))
print(type(b))

def c():
    yield 3

print(type(c))
print(isinstance(c, FunctionType))

def d():
    return (x for x in [4])

for i in d():
    print(i)
