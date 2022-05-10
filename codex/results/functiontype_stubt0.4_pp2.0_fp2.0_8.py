from types import FunctionType
a = (x for x in [1])
print(type(a))
print(a.__next__())
print(a.__next__())

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(a.__next__())

# print(a.__next__())

b = (x for x in [1, 2, 3])
print(b.__next__())
print(b.__next__())
print(b.__next__())

# print(b.__next__())

def a():
    yield 1
    yield 2
    yield 3

c = a()
print(c.__next__())
print(c.__next__())
print(c.__next__())

# print(c.__next__())

def a():
    yield 1
    yield 2
    yield 3

c = a()
print(next(c))
print(next(c))
print(next(c))

# print(next(c))

# print(next(c))

def a():
    yield 1
