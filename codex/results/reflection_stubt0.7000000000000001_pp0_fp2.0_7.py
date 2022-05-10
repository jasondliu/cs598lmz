fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__name__ = 'gi'
fn.__qualname__ = 'gi'
fn()

# Test a generator which yields a callable
def f(): yield lambda: None
g = f()
fn = next(g)
gi = (i for i in ())
fn.__code__ = gi
fn.__name__ = 'gi'
fn.__qualname__ = 'gi'
fn()

# Test a generator expression
ge = (i for i in ())
fn.__code__ = ge
fn.__name__ = 'ge'
fn.__qualname__ = 'ge'
fn()

# Test a nested generator expression
ge1 = (i for i in ())
ge2 = (i for i in ge1)
ge3 = (i for i in ge2)
fn.__code__ = ge3
fn.__name__ = 'ge3'
fn.__qualname__ = 'ge3'
fn()

# Test a list comprehension
lc = [i for i in ()]
fn.__code__ = lc
fn.__name
