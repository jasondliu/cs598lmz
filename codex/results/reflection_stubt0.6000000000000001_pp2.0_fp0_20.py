fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #6526: crash when running a generator which has been run to completion
# until the frame is garbage collected and the frame's generator is
# reallocated.

def f():
    def g():
        yield 1
        yield 2
    f = g()
    f.__next__()
    f.__next__()
    f.__next__()
    del f
    return g()

for x in f():
    pass

# Issue #6528: yield from fails when there are finally clauses.

def f():
    try:
        yield
    finally:
        pass

for x in (x for x in ()):
    pass

# Issue #6529: yield from fails when there are finally clauses.

def f():
    try:
        yield
    finally:
        pass

for x in f():
    pass

# Issue #6530: yield from fails when there are finally clauses.

def f():
    try:
        yield 1
    finally:
        pass

def g():

