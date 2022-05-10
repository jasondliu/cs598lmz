from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(a.__next__())
print(a.__next__())

def foo():
    yield 1
    yield 2
    yield 3

print(type(foo))
print(foo)
print(type(foo()))
print(foo())

print(isinstance(foo, FunctionType))
print(isinstance(foo(), GeneratorType))

def foo2():
    yield 1
    yield 2
    yield 3
    return 'foo2'

f = foo2()
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())


def foo3():
    yield 1
    yield 2
    yield 3
    return 'foo3'

f = foo3()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
