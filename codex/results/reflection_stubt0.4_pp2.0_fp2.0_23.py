fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #13897: Don't crash when an exception is raised in a generator
# frame and the generator is resumed after the frame is freed.
def f():
    yield
    raise StopIteration

def g():
    try:
        yield from f()
    except StopIteration:
        pass

def h():
    yield from g()

def i():
    try:
        yield from h()
    except StopIteration:
        pass

i().__next__()

# Issue #13897: Don't crash when an exception is raised in a generator
# frame and the generator is resumed after the frame is freed.
def f():
    yield
    raise StopIteration

def g():
    try:
        yield from f()
    except StopIteration:
        pass

def h():
    yield from g()

def i():
    try:
        yield from h()
    except StopIteration:
        pass

i().__next__()

# Issue #13897: Don't crash when an
