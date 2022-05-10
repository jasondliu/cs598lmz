fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16077: test that a generator can be used as a code object
# (this is a regression test for a bug that was fixed in 2.7.5)
def f():
    yield
f.__code__ = f()
f()

# Issue #16077: test that a generator can be used as a code object
# (this is a regression test for a bug that was fixed in 2.7.5)
def f():
    yield
f.__code__ = f()
f()

# Issue #16077: test that a generator can be used as a code object
# (this is a regression test for a bug that was fixed in 2.7.5)
def f():
    yield
f.__code__ = f()
f()

# Issue #16077: test that a generator can be used as a code object
# (this is a regression test for a bug that was fixed in 2.7.5)
def f():
    yield
f.__code__ = f()
f()

# Issue #16077: test
