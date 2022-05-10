import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() returns correctly for weak references.
a = weakref.ref(B(5))
if a() is not None:
    print "NOT OK 1"
b = weakref.ref(A(5))
if b() is not None:
    print "NOT OK 2"

gc.collect()
if a() is not None:
    print "NOT OK 3"
if b() is not None:
    print "NOT OK 4"

# Test gc.collect() returns correctly with no arguments.
a_refs = [weakref.ref(A()) for i in range(128)]
b_refs = [weakref.ref(B()) for i in range(16)]
for r in a_refs + b_refs:
    if r() is None:
        print "NOT OK 5"
c = gc.collect()
if c != 0:
    print "NOT OK 6", c
for r in a_refs + b_refs:
    if r() is None:
        print "NOT OK 7"

print "OK"
