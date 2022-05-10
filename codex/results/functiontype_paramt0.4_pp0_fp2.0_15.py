from types import FunctionType
list(FunctionType(lambda: None, globals(), 'func') for _ in range(2))

def f():
    yield 1
    yield 2
    yield 3

def g():
    yield from f()

list(g())

def f():
    for i in range(4):
        yield i

def g():
    yield from f()

list(g())

def f():
    for i in range(4):
        yield i

def g():
    yield from f()
    yield from f()

list(g())

def f():
    for i in range(4):
        yield i

def g():
    yield from f()
    yield from f()

list(g())

def f():
    for i in range(4):
        yield i

def g():
    yield from f()
    yield from f()

list(g())

def f():
    for i in range(4):
        yield i

def g():
    yield from f()
    yield from f()

list(g())

def f():
