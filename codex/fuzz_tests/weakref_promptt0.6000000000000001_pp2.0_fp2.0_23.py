import weakref
# Test weakref.ref

class E:
    pass

class F:
    pass

e = E()
f = F()
e.f = f
f.e = e

eid = id(e)
fid = id(f)

r = weakref.ref(e)
r2 = weakref.ref(f)
e.f = None
f.e = None
e = None
f = None

assert r() is None
assert r2() is None
