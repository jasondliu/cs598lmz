fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

def g():
    yield

def f():
    g()

f()

def f():
    def g():
        yield
    g()

f()

def f():
    yield

f()

def f():
    g = (i for i in ())
    g.__next__()

f()

def f():
    g = (i for i in ())
    g.send(None)

f()

def f():
    g = (i for i in ())
    g.throw(StopIteration)

f()

def f():
    g = (i for i in ())
    g.close()

f()

def f():
    def g():
        yield
    g = g()
    g.__next__()

f()

def f():
    def g():
        yield
    g = g()
    g.send(None)

f()

def f():
    def g():
        yield
    g = g()
    g.throw(Stop
