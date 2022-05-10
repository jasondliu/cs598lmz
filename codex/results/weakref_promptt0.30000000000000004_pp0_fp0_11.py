import weakref
# Test weakref.ref(x)

class C:
    pass

c = C()
r = weakref.ref(c)
assert r() is c

c2 = C()
r2 = weakref.ref(c2)
assert r2() is c2

assert r() is not r2()

# Test weakref.ref(x, callback)

class C2:
    pass

c = C2()
l = []
def callback(arg):
    l.append(arg)
r = weakref.ref(c, callback)
assert r() is c

del c
assert len(l) == 1
assert l[0] is r()

# Test weakref.proxy(x)

class C3:
    pass

c = C3()
p = weakref.proxy(c)
assert p is c

c2 = C3()
p2 = weakref.proxy(c2)
assert p2 is c2

assert p is not p2

# Test weakref.proxy(x, callback)

class C4:
    pass
