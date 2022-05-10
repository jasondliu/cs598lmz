from types import FunctionType
a = (x for x in [1])
print(a)
print(a.__next__())
print(a.__next__())

b = (x for x in range(10))
for x in b:
    print(x)

def add(a, b):
    return a + b
print(add(1, 2))
print(add([1], [2]))

def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, list) and isinstance(b, list):
        return a + b
    else:
        raise TypeError
print(add(1, 2))
print(add([1], [2]))

def add(a, b):
    if (type(a) == int and type(b) == int):
        return a + b
    elif (type(a) == list and type(b) == list):
        return a + b
    else:
        raise TypeError
print(add(1, 2))
print(add([1], [2
