fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #15
def f():
    def g():
        yield
    yield from g()

# Issue #16
def f():
    def g():
        yield
    yield from g()

# Issue #17
def f():
    def g():
        yield
    yield from g()

# Issue #18
def f():
    def g():
        yield
    yield from g()

# Issue #19
def f():
    def g():
        yield
    yield from g()

# Issue #20
def f():
    def g():
        yield
    yield from g()

# Issue #21
def f():
    def g():
        yield
    yield from g()

# Issue #22
def f():
    def g():
        yield
    yield from g()

# Issue #23
def f():
    def g():
        yield
    yield from g()

# Issue #24
def f():
    def g():
        yield
    yield from g()

# Issue #25
def f():
