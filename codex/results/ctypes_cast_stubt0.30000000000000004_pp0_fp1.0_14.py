import ctypes
ctypes.cast(0, ctypes.py_object)

# ____________________________________________________________

class X(object):
    pass

def f():
    return X()

def g():
    return f()

def h():
    return g()

def i():
    return h()

def j():
    return i()

def k():
    return j()

def l():
    return k()

def m():
    return l()

def n():
    return m()

def o():
    return n()

def p():
    return o()

def q():
    return p()

def r():
    return q()

def s():
    return r()

def t():
    return s()

def u():
    return t()

def v():
    return u()

def w():
    return v()

def x():
    return w()

def y():
    return x()

def z():
    return y()

def aa():
    return z()

def bb():
   
