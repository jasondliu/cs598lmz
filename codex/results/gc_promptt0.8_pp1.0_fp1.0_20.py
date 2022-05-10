import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
HeapType = type(sys.getobjects(0))
h = HeapType()
def callback(x):
    print("Callback:", x)
def f(n):
    print("f", n)
    if n >= 0:
        f(n-1)
        print("end f", n)
        return h.index(callback(n))
    return None
h.insert(0, f(1))
h.index(callback(2))
h.insert(0, h.index(callback(3)))
h.index(callback(4))
h.insert(0, f(5))
h.index(callback(6))
g = gc.collect()
# Test writetrack
d = weakref.WeakKeyDictionary()
# Test weakref.WeakKeyDictionary
def f():
    v = []
    class C:
        pass
    c = C()
    v.append(c)
    d[c] = v
    del c
    gc.collect()
    return v[0]
def g():
    v = []
