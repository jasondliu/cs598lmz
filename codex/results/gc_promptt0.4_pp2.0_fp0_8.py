import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "<A %s>" % self.name

def f():
    a = A("a")
    b = A("b")
    c = A("c")
    a.b = b
    b.a = a
    b.c = c
    c.b = b
    return c

gc.collect()
print gc.garbage
print gc.collect()
print gc.garbage

c = f()
print gc.collect()
print gc.garbage

del c
print gc.collect()
print gc.garbage

# Test weakrefs

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "<A %s>" % self.name

def f():
    a = A("a")

