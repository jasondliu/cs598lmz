import weakref
# Test weakref.ref() and weakref.proxy()

# Test a cycle with a ref and a proxy.

class C:
    pass

o = C()

def f(x):
    return x()

def g(x):
    return x.__class__

def h(x):
    return x.foo

def i(x):
    return x.foo()

def j(x):
    return x.foo.__class__

def k(x):
    return x.foo.foo

def l(x):
    return x.foo.foo()

def m(x):
    return x.foo.foo.__class__

def n(x):
    return x.foo.foo.foo

def o(x):
    return x.foo.foo.foo()

def p(x):
    return x.foo.foo.foo.__class__

def q(x):
    return x.foo.foo.foo.foo

def r(x):
    return x.foo.foo.foo.foo()

def s(
