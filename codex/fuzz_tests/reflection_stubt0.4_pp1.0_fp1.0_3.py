fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# xfail: https://github.com/python/mypy/issues/1270
def fn():
    pass
fn.__code__ = (i for i in ())
fn()
