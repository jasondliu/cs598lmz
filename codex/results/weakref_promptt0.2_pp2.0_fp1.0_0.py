import weakref
# Test weakref.ref()

class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'C(%r)' % self.x

def f():
    c = C(1)
    r = weakref.ref(c)
    print(r)
    print(r())
    print(r() is c)
    print(r() is None)
    del c
    print(r() is None)

f()

# Test weakref.proxy()

def f():
    c = C(1)
    p = weakref.proxy(c)
    print(p)
    print(p.x)
    print(p.x == c.x)
    print(p is c)
    print(p is None)
    del c
    try:
        print(p)
    except ReferenceError:
        print('ReferenceError')

f()

# Test weakref.getweakrefcount()

def f():
    c = C(1)
    r = weakref
