fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27093: Crash when a generator function is called with a keyword
# argument.
def f(a, b=1):
    yield a
    yield b

f(1)
f(a=1)
f(1, 2)
f(a=1, b=2)

# Issue #27093: Crash when a generator function is called with a keyword
# argument.
def f(a, b=1):
    yield a
    yield b

f(1)
f(a=1)
f(1, 2)
f(a=1, b=2)

# Issue #27093: Crash when a generator function is called with a keyword
# argument.
def f(a, b=1):
    yield a
    yield b

f(1)
f(a=1)
f(1, 2)
f(a=1, b=2)

# Issue #27093: Crash when a generator function is called with a keyword
# argument.
def f(a, b=1):

