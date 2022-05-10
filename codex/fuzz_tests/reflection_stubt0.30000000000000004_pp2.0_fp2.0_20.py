fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #14963: test that a generator is not closed if it is
# used as a code object.
def f():
    yield 1
f.__code__ = f()
f()

# Issue #14963: test that a generator is not closed if it is
# used as a code object.
def f():
    yield 1
f.__code__ = f()
f()

# Issue #14963: test that a generator is not closed if it is
# used as a code object.
def f():
    yield 1
f.__code__ = f()
f()

# Issue #14963: test that a generator is not closed if it is
# used as a code object.
def f():
    yield 1
f.__code__ = f()
f()

# Issue #14963: test that a generator is not closed if it is
# used as a code object.
def f():
    yield 1
f.__code__ = f()
f()

# Issue #14963: test that a generator is not
