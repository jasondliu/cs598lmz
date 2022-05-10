gi = (i for i in ())
# Test gi.gi_code

def g():
    yield 1

gi = g()
# Test gi.gi_frame

def f():
    for i in range(10):
        yield i

gi = f()
# Test gi.gi_running

def g():
    yield 1

gi = g()
next(gi)
# Test gi.gi_yieldfrom

def f():
    yield from range(10)

gi = f()
# Test gi.gi_weakreflist

def g():
    yield 1

gi = g()
# Test gi.__del__

def g():
    yield 1

gi = g()
# Test gi.__length_hint__

def g():
    yield 1

gi = g()
# Test gi.__name__

def g():
    yield 1

gi = g()
# Test gi.close

def g():
    yield 1

gi = g()
# Test gi.send

def g():
    yield 1

gi = g()
#
