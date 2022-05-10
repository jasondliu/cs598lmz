import weakref
# Test weakref.ref()
class C:
    pass
o = C()
r = weakref.ref(o)
assert r() is o

# Test weakref.proxy()
import weakref
class C:
    pass
o = C()
p = weakref.proxy(o)
assert p is o

# Test weakref.getweakrefs()
class C:
    pass
o = C()
r = weakref.ref(o)
r2 = weakref.ref(o)
c = weakref.getweakrefcount(o)
assert c == 2
l = weakref.getweakrefs(o)
assert l == [r, r2]

# Test weakref.ref() with a callable
class C:
    pass
def f():
    pass
o = C()
f.o = o
r = weakref.ref(f)
assert r() is f
assert r().o is o

# Test weakref.proxy() with a callable
class C:
    pass
def f():
    pass
o = C()
f.o = o

