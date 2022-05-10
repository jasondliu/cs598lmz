fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
fn.__code__.co_varnames = ('bar',)
foo = lambda bar: bar
fn.func_code = foo.func_code
fn()  # Issue #22798.
del fn
del gi


def f(a, (b, c), *d, **e):
    pass

def g(**kwargs):
    pass

def h(a, b=1, *args, **kwargs):
    pass

def i(a, b=1, c=2, *args, **kwargs):
    pass

def j(a, b, c=1, d=2, *args, **kwargs):
    pass

def k(a, b=1, c=2, d=3, e=4, f=5, *args, **kwargs):
    pass

def l(a, b=1, c=2, d=3, e=4, f=5, g=6, h=7, i=8, *args, **
