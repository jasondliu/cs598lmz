fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #5: https://github.com/python/cpython/issues/5
def f():
    def g():
        return 1
    return g

f()()

# issue #6: https://github.com/python/cpython/issues/6
def f():
    def g():
        return 1
    return g

f()()

# issue #7: https://github.com/python/cpython/issues/7
def f():
    def g():
        return 1
    return g

f()()

# issue #8: https://github.com/python/cpython/issues/8
def f():
    def g():
        return 1
    return g

f()()

# issue #9: https://github.com/python/cpython/issues/9
def f():
    def g():
        return 1
    return g

f()()

# issue #10: https://github.com/python/cpython/issues/10
def f():
    def g():
        return 1

