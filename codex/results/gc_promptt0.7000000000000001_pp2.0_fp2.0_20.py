import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() being called twice
l = []

# issue 2
class Foo(object):
    pass

def callback(wr):
    print("WR", wr)
    l.append(wr)

f = Foo()
wr = weakref.ref(f, callback)

f.garbage = f
f.garbage2 = f
f.garbage3 = f
wr = weakref.ref(f)
f = None
gc.collect()
gc.collect()
gc.collect()

gc.garbage


# issue 1
class Foo(object):
    pass


def callback(wr):
    print("WR", wr)
    l.append(wr)


f = Foo()
wr = weakref.ref(f, callback)

f.garbage = f
f.garbage2 = f
f.garbage3 = f
wr = weakref.ref(f)
f = None
gc.collect()
gc.collect()
gc.collect()

gc.garbage
