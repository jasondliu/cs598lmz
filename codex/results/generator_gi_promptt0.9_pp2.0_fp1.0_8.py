gi = (i for i in ())
# Test gi.gi_code attribute
def f(): yield 1

gi = f()
TestError(gi.gi_code != f.__code__, "gi.gi_code != f.__code__")
# Test gi.gi_frame attribute

def f():
    x = 1
    gi = (i for i in ())
    if hasattr(gi, 'gi_frame'):
        TestError(gi.gi_frame != sys._getframe(), "Unexpected gi.gi_frame")
    yield 2
    TestError(gi.gi_frame != sys._getframe(), "Unexpected gi.gi_frame")

gi = f()

# Test gi_running exception

def f():
    gi = (i for i in())
    yield 1
    try:
        gi.gi_running
        raise TestFailed("gi_running failed to raise ValueError")
    except ValueError:
        pass
    yield 2

gi = f()

# Test chained generators
def chain1():
    yield 0
    yield from chain2()
    yield 3
def chain2
