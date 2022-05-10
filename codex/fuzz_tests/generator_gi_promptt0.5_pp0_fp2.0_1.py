gi = (i for i in ())
# Test gi.gi_code, gi.gi_frame and gi.gi_running
next(gi)
# Test gi.gi_frame
del gi

# Test that StopIteration is raised when exiting a generator
# that raises an exception.
def gen():
    yield 1
    raise StopIteration
def f():
    try:
        g = gen()
        next(g)
        raise AssertionError
    except StopIteration:
        pass
f()

def gen():
    yield 1
    yield 2
def f():
    g = gen()
    next(g)
    try:
        next(g)
        raise AssertionError
    except StopIteration:
        pass
    try:
        next(g)
        raise AssertionError
    except StopIteration:
        pass
f()

def gen():
    try:
        yield 1
    except Exception:
        yield 2
    yield 3
def f():
    g = gen()
    next(g)
    try:
        g.throw(Exception)
        raise AssertionError

