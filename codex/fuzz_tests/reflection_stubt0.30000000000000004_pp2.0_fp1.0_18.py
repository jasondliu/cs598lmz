fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator can be used as a code object.
def f():
    def g():
        yield 1
    return g

f().__code__ is f().__code__

# Test that a generator can be used as a code object.
def f():
    def g():
        yield 1
    return g

f().__code__ is f().__code__

# Test that a generator can be used as a code object.
def f():
    def g():
        yield 1
    return g

f().__code__ is f().__code__

# Test that a generator can be used as a code object.
def f():
    def g():
        yield 1
    return g

f().__code__ is f().__code__

# Test that a generator can be used as a code object.
def f():
    def g():
        yield 1
    return g

f().__code__ is f().__code__

# Test that a generator can be used as a code object.
def f():
    def g():

