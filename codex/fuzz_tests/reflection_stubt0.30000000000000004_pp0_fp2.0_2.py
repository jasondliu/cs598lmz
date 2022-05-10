fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #26
def f():
    yield from g()

def g():
    yield from h()

def h():
    yield from i()

def i():
    yield from j()

def j():
    yield from k()

def k():
    yield from l()

def l():
    yield from m()

def m():
    yield from n()

def n():
    yield from o()

def o():
    yield from p()

def p():
    yield from q()

def q():
    yield from r()

def r():
    yield from s()

def s():
    yield from t()

def t():
    yield from u()

def u():
    yield from v()

def v():
    yield from w()

def w():
    yield from x()

def x():
    yield from y()

def y():
    yield from z()

def z():
    yield from aa()

def aa():
    yield from ab()

