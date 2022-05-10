import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

# Create a list of objects to collect
def f():
    class A: pass
    class B: pass
    class C: pass
    class D: pass
    class E: pass
    class F: pass
    class G: pass
    class H: pass
    class I: pass
    class J: pass
    class K: pass
    class L: pass
    alist = []
    alist.append(A())
    alist.append(B())
    alist.append(C())
    alist.append(D())
    alist.append(E())
    alist.append(F())
    alist.append(G())
    alist.append(H())
    alist.append(I())
    alist.append(J())
    alist.append(K())
    alist.append(L())
    return alist

# Create a list of weak references to the objects in alist
def g(alist):
    blist = []
    for a in alist:
        blist.append(weakref.
