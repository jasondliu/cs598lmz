import weakref
# Test weakref.ref() and weakref.ProxyType()

class C:
    pass

class D:
    pass

o = C()

r1 = weakref.ref(o)
assert r1() is o

r2 = weakref.ref(r1)
assert r2() is r1

r3 = weakref.ref(r2)
assert r3() is r2

r4 = weakref.ref(r3)
assert r4() is r3

o2 = D()

r5 = weakref.ref(o2)
assert r5() is o2

r6 = weakref.ref(r5)
assert r6() is r5

r7 = weakref.ref(r6)
assert r7() is r6

r8 = weakref.ref(r7)
assert r8() is r7

del o
del r1
del r2
del r3
del r4
r8()
r7()
r6()
r5()
del o2
del r5
del r6
del r7
