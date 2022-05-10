import weakref
# Test weakref.ref, weakref.proxied, weakref.proxy
import weakref

class C:
    pass

o = C()
r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1
assert weakref.getweakrefs(o) == [r]

p = weakref.proxy(o)
assert weakref.getweakrefcount(o) == 2
rs = weakref.getweakrefs(o)
assert len(rs) == 2
assert rs[0] == r or rs[1] == r
assert rs[0] == p or rs[1] == p
assert rs[0] != rs[1]

r2 = weakref.ref(o)
assert weakref.getweakrefcount(o) == 3
rs = weakref.getweakrefs(o)
assert rs == [r, p, r2] or rs == [r2, p, r]

assert repr(r).startswith("<weakref at")
assert repr(r2).startswith("<weakref at")
assert repr(
