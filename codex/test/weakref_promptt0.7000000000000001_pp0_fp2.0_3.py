import weakref
# Test weakref.ref() - for partial and non-partial references, using three
# difference types: instance, class, and dictionary.

class C(object):
    pass

def f(x):
    global r
    r = weakref.ref(x)

def g(x):
    global p
    p = weakref.ref(x)

def h(x):
    global q
    q = weakref.ref(x, lambda y: None)

# Create a weak reference to a class.
c = C
f(c)
assert r() is c

# Create a weak reference to an instance.
c = C()
f(c)
assert r() is c

# Create a weak reference to a dictionary.
c = {}
f(c)
assert r() is c

# Create a partial weak reference to a class.
c = C
g(c)
assert p() is c

# Create a partial weak reference to an instance.
c = C()
g(c)
assert p() is c

# Create a partial weak reference to a dictionary.
c = {}
