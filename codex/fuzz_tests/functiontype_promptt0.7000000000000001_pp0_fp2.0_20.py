import types
# Test types.FunctionType
try:
    types.FunctionType
except AttributeError:
    print('SKIP')
    raise SystemExit

def f(x):
    return x

def g(x):
    return x+1

def h(x):
    return 'hello ' + x

def i(x, y):
    return str(x) + y

def j(x):
    return x

def k(x):
    return x

def l(x):
    return x

def m(x):
    return x

def n(x):
    return x

def o(x):
    return x

def p(x):
    return x

def q(x):
    return x

def r(x):
    return x

def s(x):
    return x

def t(x):
    return x

def u(x):
    return x

def v(x):
    return x

def w(x):
    return x

def x(x):
    return x

def y(x
