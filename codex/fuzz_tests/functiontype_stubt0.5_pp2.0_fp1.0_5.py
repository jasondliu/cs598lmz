from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(a.__next__())
print(a.__next__())

print()

def f():
    print('a')
    yield 1
    print('b')
    yield 2
    print('c')
    yield 3

print(isinstance(f, FunctionType))
print(isinstance(f(), GeneratorType))

g = f()
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

print()

def f():
    yield 1
    yield 2
    yield 3

g = f()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

print()

def f():
    yield 1
    yield 2
    yield 3

g = f()
print(g.__next__())
print(g.__next__())
print
