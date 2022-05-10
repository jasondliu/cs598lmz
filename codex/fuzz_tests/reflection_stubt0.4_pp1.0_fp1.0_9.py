fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_generator_finalization
def f():
    yield 42
    yield None

def g():
    yield from f()

list(g())

# test_generator_finalization_2
def f():
    yield 42
    yield None

def g():
    yield from f()

g()

# test_generator_finalization_3
def f():
    yield 42
    yield None

def g():
    yield from f()

for x in g():
    pass

# test_generator_finalization_4
def f():
    yield 42
    yield None

def g():
    yield from f()

def h():
    yield from g()

for x in h():
    pass

# test_generator_finalization_5
def f():
    yield 42
    yield None

def g():
    yield from f()

def h():
    yield from g()

list(h())

# test_generator_finalization_6
def f():
    yield
