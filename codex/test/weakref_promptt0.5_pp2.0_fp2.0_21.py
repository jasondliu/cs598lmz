import weakref
# Test weakref.ref
import weakref

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

o2 = C()
r2 = weakref.ref(o2, lambda x: None)
assert r2() is o2

r3 = weakref.ref(o2, lambda x: x)
assert r3() is o2

r4 = weakref.ref(o2, lambda x: x)
assert r4() is o2

r5 = weakref.ref(o, lambda x: x)
assert r5() is o

r6 = weakref.ref(o, lambda x: x)
assert r6() is o

r7 = weakref.ref(o, lambda x: x)
assert r7() is o

r8 = weakref.ref(o, lambda x: x)
assert r8() is o

r9 = weakref.ref(o, lambda x: x)
assert r9() is o

r10 = weakref.ref(o, lambda x: x)
