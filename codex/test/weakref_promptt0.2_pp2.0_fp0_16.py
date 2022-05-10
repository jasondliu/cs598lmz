import weakref
# Test weakref.ref()

def f():
    return 42

def g():
    return [43]

def h():
    return (44,)

def i():
    return {45: 46}

def j():
    return {47}

def k():
    return frozenset([48])

def l():
    return weakref.ref(f)

def m():
    return weakref.ref(g)

def n():
    return weakref.ref(h)

def o():
    return weakref.ref(i)

def p():
    return weakref.ref(j)

def q():
    return weakref.ref(k)

def r():
    return weakref.ref(l)

def s():
    return weakref.ref(m)

def t():
    return weakref.ref(n)

def u():
    return weakref.ref(o)

def v():
    return weakref.ref(p)

def w():
    return weakref.ref(q)

