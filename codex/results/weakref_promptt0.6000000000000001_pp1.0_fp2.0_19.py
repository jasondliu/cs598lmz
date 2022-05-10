import weakref
# Test weakref.ref(None)

def doit(r):
    print(r)
    print(r())
    print(r is None)

r = weakref.ref(None)
doit(r)
assert r() is None

r = weakref.ref(lambda: None)
doit(r)
assert r() is None

# Test weakref.ref(callable)

class C(object):
    def __call__(self):
        return None

r = weakref.ref(C())
doit(r)
assert r() is None

# Test weakref.proxy(callable)

class C(object):
    def __call__(self):
        return None

p = weakref.proxy(C())
print(p)
print(p())
print(p is None)
assert p() is None

# Test weakref.getweakrefcount on callable

class C(object):
    def __call__(self):
        return None

c = C()
assert weakref.getweakrefcount(c) == 0

