fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #8
# https://github.com/python/mypy/issues/8

def f(x: int) -> int:
    return x

f(1)
f('a')

# Issue #9
# https://github.com/python/mypy/issues/9

class A:
    pass

class B(A):
    pass

def f(a: A) -> None:
    pass

f(A())
f(B())

# Issue #10
# https://github.com/python/mypy/issues/10

def f(x: int) -> int:
    return x

f(1)
f('a')

# Issue #11
# https://github.com/python/mypy/issues/11

def f(x: int) -> int:
    return x

f(1)
f('a')

# Issue #12
# https://github.com/python/mypy/issues/12

def f(x: int) -> int:
    return
