fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified when the generator is closed
# and that the generator is not closed when the code object is modified.
def f():
    yield 1
    yield 2
    yield 3

def g():
    yield 4
    yield 5
    yield 6

fn.__code__ = f.__code__
fn()
fn.__code__ = g.__code__
fn()

# Test that the code object is not modified when the generator is closed
# and that the generator is not closed when the code object is modified.
def f():
    yield 1
    yield 2
    yield 3

def g():
    yield 4
    yield 5
    yield 6

fn.__code__ = f.__code__
fn()
fn.__code__ = g.__code__
fn()

# Test that the code object is not modified when the generator is closed
# and that the generator is not closed when the code object is modified.
def f():
    yield 1
    yield 2
    yield 3

def g():
    yield 4

