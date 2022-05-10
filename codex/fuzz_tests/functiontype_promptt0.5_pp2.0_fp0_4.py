import types
# Test types.FunctionType
# See if we can detect when a function is called
def f(x):
    return x

def g(f, x):
    return f(x)

def h(x):
    return g(f, x)

def i(x):
    return h(x)

def j(x):
    return i(x)

def k(x):
    return j(x)

def l(x):
    return k(x)

def m(x):
    return l(x)

def n(x):
    return m(x)

def o(x):
    return n(x)

def p(x):
    return o(x)

def q(x):
    return p(x)

def r(x):
    return q(x)

def s(x):
    return r(x)

def t(x):
    return s(x)

def u(x):
    return t(x)

def v(x):
    return u(x)

def w(
