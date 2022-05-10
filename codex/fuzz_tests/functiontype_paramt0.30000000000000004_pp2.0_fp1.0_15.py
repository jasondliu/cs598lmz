from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'foo'))

# Test for issue #30984:
def f():
    def g():
        yield
    yield from g()

# Test for issue #30984:
def f():
    def g():
        yield from g()
    yield from g()

# Test for issue #30984:
def f():
    def g():
        yield from g()
    yield from g()

# Test for issue #30984:
def f():
    def g():
        yield from g()
    yield from g()

# Test for issue #30984:
def f():
    def g():
        yield from g()
    yield from g()

# Test for issue #30984:
def f():
    def g():
        yield from g()
    yield from g()

# Test for issue #30984:
def f():
    def g():
        yield from g()
    yield from g()

# Test for issue #30984:
def f():
    def g():
       
