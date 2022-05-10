fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #3764
def f():
    def g():
        yield 1
    return g()

assert isinstance(f(), types.GeneratorType)

# issue #3770
def f():
    def g():
        yield 1
    return g

assert isinstance(f()(), types.GeneratorType)

# issue #3775
def f():
    def g():
        yield 1
    return g

def h():
    def g():
        yield 2
    return g

assert f()() == h()()

# issue #3780
def f():
    def g():
        yield 1
    return g

def h():
    def g():
        yield 2
    return g

assert f().__code__ == h().__code__

# issue #3783
def f():
    def g():
        yield 1
    return g

def h():
    def g():
        yield 2
    return g

assert f().__code__.co_consts == h().__code__.co_
