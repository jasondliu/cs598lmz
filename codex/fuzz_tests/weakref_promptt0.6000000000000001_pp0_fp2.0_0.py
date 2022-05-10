import weakref
# Test weakref.ref() with lambda expressions.
import gc

def f():
    return 42


def g(x):
    return lambda: x


def h(x):
    return lambda y: x + y


for i in range(2):
    x = f()
    r = weakref.ref(x)
    c = r()
    d = c()
    e = d()
    print(e)
    gc.collect()
    print(r() is None, c() is None, d() is None, e is None)
    x = g(42)
    r = weakref.ref(x)
    c = r()
    d = c()
    e = d()
    print(e)
    gc.collect()
    print(r() is None, c() is None, d() is None, e is None)
    x = h(42)
    r = weakref.ref(x)
    c = r()
    d = c(100)
    e = d(200)
    print(e)
    gc.collect()

