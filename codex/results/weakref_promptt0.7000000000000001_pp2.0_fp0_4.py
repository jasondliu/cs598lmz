import weakref
# Test weakref.reference() and weakref.getweakrefcount()
import _weakref

class C:
    pass

o = C()
r = weakref.ref(o)
wr = weakref.getweakrefcount(o)

if wr != 1:
    raise RuntimeError

class Nasty:
    def __del__(self):
        import gc
        gc.collect()

def f():
    a = Nasty()
    w = weakref.ref(a)
    a.x = w

try:
    f()
except RuntimeError:
    pass
else:
    raise RuntimeError

class D(weakref.WeakKeyDictionary):
    pass

class E:
    pass

e = E()
d = D()
d[e] = 1

if d[e] != 1:
    raise RuntimeError

if len(d) != 1:
    raise RuntimeError

del e

if len(d) != 0:
    raise RuntimeError

# test callback handling

class X:
    pass

def f(
