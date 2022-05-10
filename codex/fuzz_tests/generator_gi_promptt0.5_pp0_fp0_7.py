gi = (i for i in ())
# Test gi.gi_code is None

gi = (i for i in ())
# Test gi.gi_frame is None

gi = (i for i in ())
# Test gi.gi_running is False

gi = (i for i in ())
# Test gi.gi_yieldfrom is None

def f():
    yield from range(5)
gi = f()
# Test gi.gi_code is f.__code__

def f():
    yield from range(5)
gi = f()
# Test gi.gi_frame is not None

def f():
    yield from range(5)
gi = f()
# Test gi.gi_running is False

def f():
    yield from range(5)
gi = f()
# Test gi.gi_yieldfrom is None

def f():
    yield from g()
def g():
    yield from range(5)
gi = f()
# Test gi.gi_code is f.__code__

def f():
    yield from g()
def g():
    yield from range(5
