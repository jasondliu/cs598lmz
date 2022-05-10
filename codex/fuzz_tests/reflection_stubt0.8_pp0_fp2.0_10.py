fn = lambda: None
gi = (i for i in ())
fn.__code__ = _code(0)
gi.gi_code = fn.__code__
inspect.getmro(gi)

def f():
    yield True
    yield from g
inspect.getclosurevars(f)

def f(a=1, b): pass
inspect.signature(f)

def f():
    def g():
        pass
    return g
inspect.getsource(f().__code__)
inspect.getsource(f)

def f(a): ...
inspect.signature(f)
inspect.signature(f).parameters['a'].default

def f():
    def g():
        pass
    return g
inspect.getdoc(f())
inspect.getdoc(f)

def f(a):
    """
    Documentation for f
    """
inspect.getdoc(f)

def f():
    """
    Documentation for f
    """
    def g():
        pass
    return g
inspect.getdoc(f())
inspect.getdoc(f)


