import weakref
# Test weakref.ref()
class C:
    pass
o = C()
r = weakref.ref(o)
r
r() is o
r() is o
r() is o
r() is o
r() is o
r
r() is o
del o
r
r()
r() is None
r() is None
r() is None
r()
r()
r() is None
r() is None
r() is None
r()
r()
r() is None
r() is None
r() is None
r()
r()
r() is None
r() is None
r() is None
# Test weakref.WeakValueDictionary
import weakref
d = {}
class C:
    pass
c1 = C()
c2 = C()
c3 = C()
c4 = C()
c5 = C()
d[1] = c1
d[2] = c2
d[3] = c3
d[4] = c4
d[5] = c5
d
dd = weakref.WeakValueDictionary(d)
dd
