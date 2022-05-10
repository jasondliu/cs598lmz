from types import FunctionType
a = (x for x in [1])
type(a)

isinstance(a, GeneratorType)
isinstance(a, IteratorType)

def my_gen():
    for i in range(1,4):
        yield i
type(my_gen)
isinstance(my_gen, FunctionType)
isinstance(my_gen(), GeneratorType)

g = my_gen()
type(g)

g.__next__()
g.__next__()
g.__next__()
g.__next__()

def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a,b = b, a+b
f = fib(10)
f
isinstance(f, GeneratorType)
f.__next__()
f.__next__()
f.__next__()
f.__next__()
list(f)

# yield from

def gen():
    for i in range(10):
        yield i
    yield from (i*10 for i in range(10))
    yield from "123456789"
