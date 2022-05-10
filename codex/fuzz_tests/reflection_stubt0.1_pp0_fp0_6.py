fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23
def f():
    yield
    yield
    yield

def g():
    yield from f()

def h():
    yield from g()

def i():
    yield from h()

def j():
    yield from i()

def k():
    yield from j()

def l():
    yield from k()

def m():
    yield from l()

def n():
    yield from m()

def o():
    yield from n()

def p():
    yield from o()

def q():
    yield from p()

def r():
    yield from q()

def s():
    yield from r()

def t():
    yield from s()

def u():
    yield from t()

def v():
    yield from u()

def w():
    yield from v()

def x():
    yield from w()

def y():
    yield from x()

def z():
    yield from y()

def aa():
    yield from z
