fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #19095: Test that a generator expression can be used as the
# __code__ attribute of a function.
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #19095: Test that a generator can be used as the __code__
# attribute of a function.
def gen():
    yield 1
fn = lambda: None
fn.__code__ = gen()
fn()

# Issue #19095: Test that a generator can be used as the __code__
# attribute of a function.
def gen():
    yield 1
fn = lambda: None
fn.__code__ = gen()
fn()

# Issue #19095: Test that a generator can be used as the __code__
# attribute of a function.
def gen():
    yield 1
fn = lambda: None
fn.__code__ = gen()
fn()

# Issue #19095: Test that a generator can be used as the __code__
# attribute of a function.
def gen():
