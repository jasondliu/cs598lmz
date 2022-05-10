import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "<Foo %s>" % self.x

def f():
    l = []
    for i in range(10):
        l.append(Foo(i))
    return l

l = f()
print l
print gc.collect()
print l

l = f()
print l
print gc.collect()
print l

l = f()
print l
print gc.collect()
print l

l = f()
print l
print gc.collect()
print l

l = f()
print l
print gc.collect()
print l

l = f()
print l
print gc.collect()
print l

l = f()
print l
print gc.collect()
print l

l = f()
print l
print gc.collect()
print l

l = f()
print l
print gc.collect()
print l

l
