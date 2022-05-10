from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Issue #15
def f():
    for i in range(10):
        yield i

list(f())

# Issue #16
def f():
    yield 1
    yield 2
    yield 3

list(f())

# Issue #17
def f():
    yield 1
    yield 2
    yield 3

list(f())

# Issue #18
def f():
    yield 1
    yield 2
    yield 3

list(f())

# Issue #19
def f():
    yield 1
    yield 2
    yield 3

list(f())

# Issue #20
def f():
    yield 1
    yield 2
    yield 3

list(f())

# Issue #21
def f():
    yield 1
    yield 2
    yield 3

list(f())

# Issue #22
def f():
    yield 1
    yield 2
    yield 3

list(f())

# Issue #23
def f():
    yield 1
    yield 2

