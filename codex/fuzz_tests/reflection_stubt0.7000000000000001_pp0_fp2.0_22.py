fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
# fn()


def gen():
    try:
        yield
    except ValueError:
        pass
    try:
        yield
    except Exception:
        yield
    yield
    yield
    yield
g = gen()
next(g)
g.throw(ValueError)
next(g)
g.throw(TypeError)
next(g)
g.throw(ValueError)
g.close()


def gen():
    yield
    try:
        yield
    except ValueError:
        yield
    else:
        yield
    yield
    yield
g = gen()
next(g)
next(g)
g.throw(ValueError)
next(g)
next(g)
g.throw(ValueError)


def gen():
    try:
        yield
    except ValueError:
        yield
    except Exception:
        yield
    yield
g = gen()
next(g)
g.throw(ValueError)
next(g)
g.throw(Exception)
next(g)


def gen():
    try:

