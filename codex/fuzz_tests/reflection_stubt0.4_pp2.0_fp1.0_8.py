fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__call__()

def f(x):
    return x

def g():
    return f

def h():
    return g

def i():
    return h

def j():
    return i

def k():
    return j

def l():
    return k

def m():
    return l

def n():
    return m

def o():
    return n

def p():
    return o

def q():
    return p

def r():
    return q

def s():
    return r

def t():
    return s

def u():
    return t

def v():
    return u

def w():
    return v

def x():
    return w

def y():
    return x

def z():
    return y

def aa():
    return z

def bb():
    return aa

def cc():
    return bb

def dd():
    return cc

def ee():
    return dd

def ff():
