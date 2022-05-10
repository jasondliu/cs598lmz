fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test that a generator can be called recursively
def f():
    g()
    yield 0
def g():
    yield from f()
    yield 0

list(g())

# test that a generator can be called recursively, with "yield from" in a loop
def f():
    for i in range(2):
        g()
        yield 0
def g():
    yield from f()
    yield 0

list(g())

# test that a generator can be called recursively, with "yield from" in a loop
def f():
    for i in range(2):
        g()
        yield 0
def g():
    yield from f()
    yield 0

list(g())

# test that a generator can be called recursively, with "yield from" in a loop
def f():
    for i in range(2):
        g()
        yield 0
def g():
    yield from f()
    yield 0

list(g())

# test that a generator can be called recursively
