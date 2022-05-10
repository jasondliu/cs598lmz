fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #2
def f():
    yield 1

def g():
    yield from f()

g()

# issue #3
def f():
    yield from []

f()

# issue #4
def f():
    yield from ()

f()

# issue #5
def f():
    yield from {}

f()

# issue #6
def f():
    yield from {1: 2}

f()

# issue #7
def f():
    yield from {1, 2}

f()

# issue #8
def f():
    yield from 'abc'

f()

# issue #9
def f():
    yield from b'abc'

f()

# issue #10
def f():
    yield from bytearray(b'abc')

f()

# issue #11
def f():
    yield from memoryview(b'abc')

f()

# issue #12
def f():
    yield from range(3)

f()

