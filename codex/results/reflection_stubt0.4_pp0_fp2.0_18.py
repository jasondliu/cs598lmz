fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test for issue #3
# https://github.com/python/mypy/issues/3
def f():
    yield 1

f().__next__()

# test for issue #4
# https://github.com/python/mypy/issues/4
def g():
    yield 1

g().__iter__()

# test for issue #5
# https://github.com/python/mypy/issues/5
def h():
    yield 1

h().__length_hint__()

# test for issue #6
# https://github.com/python/mypy/issues/6
def i():
    yield 1

i().send(None)

# test for issue #7
# https://github.com/python/mypy/issues/7
def j():
    yield 1

j().throw(TypeError)

# test for issue #8
# https://github.com/python/mypy/issues/8
def k():
    yield 1

k().close()

# test for issue #9
