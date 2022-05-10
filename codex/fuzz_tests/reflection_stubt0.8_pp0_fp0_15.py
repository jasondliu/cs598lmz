fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


class CustomException(Exception):
    pass


def _gen():
    yield 1
    raise CustomException


def g():
    yield from _gen()


# The CustomException is propagated
try:
    list(g())
except CustomException:
    pass
else:
    assert False


# Calling stopiter function does nothing
def g():
    yield from (i for i in range(10))
    gi.close()


list(g())

# StopIteration is absorbed
def g():
    yield from (i for i in range(10))
    gi.throw(StopIteration)


list(g())

# __stopit__ is called
def g():
    yield from (i for i in range(10))
    gi.throw(CustomException)


try:
    list(g())
except CustomException:
    pass
else:
    assert False

# __stopit__ is called, StopIteration is absorbed
def g():
    yield from (i for i in range(10))
    gi.
