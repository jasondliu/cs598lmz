fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #29

def f():
    return 1, 2

def g():
    return f()

def h():
    return g()

print(h())

# issue #30

def f():
    yield 1

def g():
    yield from f()

def h():
    yield from g()

list(h())

# issue #31

def f():
    x = yield 1

def g():
    x = yield from f()

def h():
    x = yield from g()

next(h())

# issue #32

def f():
    yield from (1, 2)

def g():
    yield from f()

def h():
    yield from g()

list(h())

# issue #33

def f():
    yield from (i for i in ())

def g():
    yield from f()

def h():
    yield from g()

list(h())

# issue #34

def f():
    yield from (i for
