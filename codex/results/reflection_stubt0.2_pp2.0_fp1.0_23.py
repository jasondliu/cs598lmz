fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #12073: crash when a generator is called with an argument
# and the generator raises StopIteration with an argument.
def gen():
    yield 1
    raise StopIteration(2)

try:
    next(gen())
except StopIteration as e:
    assert e.value == 2

# Issue #12073: crash when a generator is called with an argument
# and the generator raises StopIteration without an argument.
def gen():
    yield 1
    raise StopIteration

try:
    next(gen())
except StopIteration as e:
    assert e.value is None

# Issue #12073: crash when a generator is called with an argument
# and the generator raises StopIteration with an argument.
def gen():
    yield 1
    raise StopIteration(2)

try:
    next(gen())
except StopIteration as e:
    assert e.value == 2

# Issue #12073: crash when a generator is called with an argument
# and the generator raises StopIteration without an argument.
