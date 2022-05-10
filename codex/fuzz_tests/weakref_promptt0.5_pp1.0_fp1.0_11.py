import weakref
# Test weakref.ref()

class C(object):
    pass

o = C()
r = weakref.ref(o)
assert r() is o

o2 = C()
r2 = weakref.ref(o2, lambda x: None)

try:
    r2()
except ReferenceError:
    pass
else:
    raise Exception("Expected ReferenceError")

del o2

try:
    r2()
except ReferenceError:
    pass
else:
    raise Exception("Expected ReferenceError")

# Test weakref.proxy()

class D(object):
    def f(self):
        return 42
    def __eq__(self, other):
        return True

o = D()
p = weakref.proxy(o)
assert p.f() == 42

assert p == 5

o2 = D()
p2 = weakref.proxy(o2, lambda x: None)

try:
    p2.f()
except ReferenceError:
    pass
else:
    raise Exception("Expected ReferenceError")

del o2
