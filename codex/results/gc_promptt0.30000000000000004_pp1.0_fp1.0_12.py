import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_referrers()
class A:
    pass

a = A()

def f():
    a = A()
    return a

b = f()

def f():
    a = A()
    return a

c = f()

def f():
    a = A()
    return a

d = f()

def f():
    a = A()
    return a

e = f()

def f():
    a = A()
    return a

f = f()

def f():
    a = A()
    return a

g = f()

def f():
    a = A()
    return a

h = f()

def f():
    a = A()
    return a

i = f()

def f():
    a = A()
    return a

j = f()

def f():
    a = A()
    return a

k = f()

def f():
    a = A()
   
