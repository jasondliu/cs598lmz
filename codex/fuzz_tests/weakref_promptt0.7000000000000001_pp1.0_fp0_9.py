import weakref
# Test weakref.ref() and weakref.proxy() with objects in call
# frames.  This can leak memory because there is no way to
# control when the reference counts of the objects go to zero
# because of the call frame.  But it should never crash.

import weakref

def foo(x, y):
    return x + y

def f(x, y):
    r = weakref.proxy(foo(x, y))
    return r

def g(x, y):
    r = weakref.ref(foo(x, y))
    return r

def h(x, y):
    r = weakref.proxy(f(x, y))
    return r

def i(x, y):
    r = weakref.ref(g(x, y))
    return r

for i in range(300):
    foo(1, 2)
    f(3, 4)
    g(5, 6)
    h(7, 8)
    i(9, 10)
    print i
