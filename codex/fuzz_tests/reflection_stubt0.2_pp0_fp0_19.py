fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_as_constant
def f():
    return 1

def g():
    return f.__code__

def h():
    return g.__code__

def i():
    return h.__code__

def j():
    return i.__code__

def k():
    return j.__code__

def l():
    return k.__code__

def m():
    return l.__code__

def n():
    return m.__code__

def o():
    return n.__code__

def p():
    return o.__code__

def q():
    return p.__code__

def r():
    return q.__code__

def s():
    return r.__code__

def t():
    return s.__code__

def u():
    return t.__code__

def v():
    return u.__code__

def w():
    return v.__code__

def x():
    return w.
