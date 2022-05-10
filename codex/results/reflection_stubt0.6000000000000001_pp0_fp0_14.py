fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# The next test is to ensure that the generator is not closed
# when the exception is raised.

def f():
    yield 1
    yield 2

g = f()
try:
    next(g)
    next(g)
    raise ZeroDivisionError()
except ZeroDivisionError:
    pytest.raises(ZeroDivisionError, g.throw, ZeroDivisionError())
    pytest.raises(ZeroDivisionError, g.throw, ZeroDivisionError())
    pytest.raises(ZeroDivisionError, g.throw, ZeroDivisionError())

# The next test is to ensure that the generator is closed
# when the exception is raised and the generator is not
# caught.

def g():
    yield 1
    yield 2
    try:
        yield 3
        yield 4
        raise ZeroDivisionError()
    except ZeroDivisionError:
        yield 5

pytest.raises(ZeroDivisionError, next, g())
pytest.raises(ZeroDivisionError, next, g())
