import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() to make sure it clears out dead weakrefs
# but also doesn't clear out live ones.
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()

l = []
for i in range(10):
    l.append(weakref.ref(l))

gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()

def f(x):
    return x*x

def g():
    return f

class C:
    def h(self):
        return f
    def foo(self):
        return 1

refs = []
for i in range(10):
    def f():
        pass
    refs.append(f)

for i in range(10):
    refs.append(weakref.ref(refs))
    refs.append(weakref.ref(refs[-1]))
    refs.append(weakref.ref(refs[-2]))
    refs
