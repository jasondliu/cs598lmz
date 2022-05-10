fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18596: crash with a chain of generators
def g1():
    yield 1
    yield from g2()
def g2():
    yield 2
    yield from g1()

list(g1())

# Issue #18596: crash with a chain of generators
def g1():
    yield 1
    yield from g2()
def g2():
    yield 2
    yield from g1()

list(g1())

# Issue #18596: crash with a chain of generators
def g1():
    yield 1
    yield from g2()
def g2():
    yield 2
    yield from g1()

list(g1())

# Issue #18596: crash with a chain of generators
def g1():
    yield 1
    yield from g2()
def g2():
    yield 2
    yield from g1()

list(g1())

# Issue #18596: crash with a chain of generators
def g1():
    yield 1
    yield from g2()
def g2():
    yield
