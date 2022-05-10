import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class Foo:
    pass

f = Foo()
wr = weakref.ref(f)

print(gc.collect())
print(gc.get_count())

del f
print(gc.collect())
print(gc.get_count())

print(wr())

print(gc.collect())
print(gc.get_count())

# Test gc.collect() with cyclic gc

l = []

class Foo:
    def __init__(self, l=l):
        self.l = l

f = Foo()
f.l.append(f)

print(gc.collect())
print(gc.get_count())

del f, l
print(gc.collect())
print(gc.get_count())

# Test gc.collect() with a dict

d = {}

print(gc.collect())
print(gc.get_count())

d[1] = 1

print(gc.collect())
print(gc.get_count())

del d
print(gc.
