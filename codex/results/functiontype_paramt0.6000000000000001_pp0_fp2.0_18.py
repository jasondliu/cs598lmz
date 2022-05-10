from types import FunctionType
list(FunctionType(f.func_code, f.func_globals))

def f():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

def g():
    yield 2
    yield 4
    yield 6
    yield 8
    yield 10

def h():
    yield 3
    yield 6
    yield 9
    yield 12
    yield 15

def squares():
    for i in iter(f()):
        yield i*i

def even():
    for i in iter(g()):
        yield i*i

def odd():
    for i in iter(h()):
        yield i*i

def even(iterable):
    for value in iterable:
        if not value % 2:
            yield value

def odd(iterable):
    for value in iterable:
        if value % 2:
            yield value

def sq(iterable):
    for value in iterable:
        yield value*value

def even(iterable):
    for value in iterable:
        if value % 2:
            continue
