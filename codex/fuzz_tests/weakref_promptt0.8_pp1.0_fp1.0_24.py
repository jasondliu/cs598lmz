import weakref
# Test weakref.ref()

def f(x):
    pass

def g(x):
    return x

def h(x):
    x.append(x)
    return x

a = f
a is f

r = weakref.ref(f)
r() is f
r()

r = weakref.ref(g)
r() is g
r()

r = weakref.ref(h)
r() is h
r()
