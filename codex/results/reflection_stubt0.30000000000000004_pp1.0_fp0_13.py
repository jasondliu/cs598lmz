fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #40
def f():
    yield

f().__next__()

# issue #41
def f():
    yield

f().__iter__()

# issue #42
def f():
    yield

f().__length_hint__()

# issue #43
def f():
    yield

f().__await__()

# issue #44
def f():
    yield

f().send(None)

# issue #45
def f():
    yield

f().throw(Exception())

# issue #46
def f():
    yield

f().close()

# issue #47
def f():
    yield

f().__next__()

# issue #48
def f():
    yield

f().__iter__()

# issue #49
def f():
    yield

f().__length_hint__()

# issue #50
def f():
    yield

f().__await__()

# issue #51
def f():
    yield
