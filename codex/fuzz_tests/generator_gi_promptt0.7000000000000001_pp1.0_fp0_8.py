gi = (i for i in ())
# Test gi.gi_code.co_filename
assert isinstance(gi.gi_code.co_filename, str)
assert isinstance(gi.gi_frame, types.FrameType)

def f():
    gi = (i for i in ())
    # Test gi.gi_code.co_filename
    assert isinstance(gi.gi_code.co_filename, str)
    assert isinstance(gi.gi_frame, types.FrameType)
f()

def g():
    yield 10
    assert False

try:
    g().send(None)
except StopIteration:
    pass

def h():
    yield 10
    return 20

assert h().send(None) == 20 # issue #2265

# issue 2233
def i():
    yield 10
    return

assert i().send(None) is None

# issue 2268
def j():
    yield 10
    return

assert j().send(None) is None

# issue 2268
def k():
    yield 10
    return

assert k().next() == 10

# issue 2
