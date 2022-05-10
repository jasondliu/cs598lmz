import gc, weakref

class C(object):
    def __init__(self):
        self.a = 1

def f():
    pass

def g():
    pass

def h():
    pass

def i():
    pass

def j():
    pass

def k():
    pass

def l():
    pass

def m():
    pass

def n():
    pass

def o():
    pass

def p():
    pass

def q():
    pass

def run(n):
    a = C()

    f()
    g()
    h()
    i()
    j()
    k()
    l()
    m()
    n()
    o()
    p()
    q()

    b = weakref.ref(a)
    f()
    g()
    h()
    i()
    j()
    k()
    l()
    m()
    n()
    o()
    p()
    q()
    a = None
    f()
    g()
    h
