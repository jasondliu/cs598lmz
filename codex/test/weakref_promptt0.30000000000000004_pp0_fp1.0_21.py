import weakref
# Test weakref.ref()

def f():
    pass

class C:
    pass

# Test weakref.ref()
r = weakref.ref(f)
assert r() is f

r = weakref.ref(C)
assert r() is C

# Test weakref.proxy()
p = weakref.proxy(f)
assert p is f

p = weakref.proxy(C)
assert p is C

class D:
    def __init__(self):
        self.x = 1

d = D()
p = weakref.proxy(d)
assert p.x == 1

d.x = 2
assert p.x == 2

# Test weakref.getweakrefcount()
assert weakref.getweakrefcount(f) == 0
assert weakref.getweakrefcount(C) == 0
assert weakref.getweakrefcount(d) == 1

# Test weakref.getweakrefs()
assert weakref.getweakrefs(f) == []
assert weakref.getweakrefs(C) == []
assert weakref
