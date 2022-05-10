fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# issue #26
def f():
    yield 1

f().__next__()

# issue #27
def f():
    yield 1

f().__iter__()

# issue #28
def f():
    yield 1

f().__length_hint__()

# issue #29
def f():
    yield 1

f().__reduce__()

# issue #30
def f():
    yield 1

f().__reduce_ex__()

# issue #31
def f():
    yield 1

f().__setstate__(None)

# issue #32
def f():
    yield 1

f().close()

# issue #33
def f():
    yield 1

f().send(None)

# issue #34
def f():
    yield 1

f().throw(None)

# issue #35
def f():
    yield 1

f().__await__()

# issue #36
def f():
    yield 1

f
