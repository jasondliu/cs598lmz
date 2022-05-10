import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

f = Foo('f')
wr = weakref.ref(f)
print(wr)
print(gc.collect())
print(wr)
print(gc.collect())
print(wr)
del f
print(gc.collect())
print(wr)
print(gc.collect())
print(wr)

# Test gc.garbage

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

f = Foo('f')
wr = weakref.ref(f)
print(wr)
print(gc.garbage)
print(gc.collect())
print(wr)
print(gc.garbage)
print(gc.collect())
print(wr)
del f
print(gc.garbage)
print(
