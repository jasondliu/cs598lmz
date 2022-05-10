fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# type-checking error
def f():
    x = 1
    y = x + 'a'

# type-checking error
def f():
    x = 1
    y = x
    y[0] = 1
