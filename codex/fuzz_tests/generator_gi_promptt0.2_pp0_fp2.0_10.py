gi = (i for i in ())
# Test gi.gi_code

def f():
    yield 1

gi = f()
# Test gi.gi_frame

def f():
    yield 1

gi = f()
next(gi)
# Test gi.gi_running

def f():
    yield 1

gi = f()
next(gi)
# Test gi.gi_yieldfrom

def f():
    yield from (1, 2, 3)

gi = f()
next(gi)
# Test gi.gi_weakreflist

def f():
    yield 1

gi = f()
# Test gi.gi_exc_state

def f():
    yield 1

gi = f()
next(gi)
# Test gi.gi_exc_traceback

def f():
    yield 1

gi = f()
next(gi)
# Test gi.gi_exc_type

def f():
    yield 1

gi = f()
next(gi)
# Test gi.gi_exc_value

def f():
    yield 1

gi
