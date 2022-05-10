import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

def f():
    print("creating cycle")
    o = []
    o.append(o)
    print("created cycle")

print("calling f()")
f()
print("calling gc.collect()")
n = gc.collect()
print("done gc.collect()")
print("gc.garbage contains %d objects" % len(gc.garbage))

# Test gc.get_objects()

def f():
    print("creating cycle")
    o = []
    o.append(o)
    print("created cycle")

print("calling f()")
f()
print("calling gc.collect()")
n = gc.collect()
print("done gc.collect()")
print("gc.garbage contains %d objects" % len(gc.garbage))

# Test gc.get_referrers()

def f():
    print("creating cycle")
    o = []
    o.append(o)
    print("created cycle")

print("calling f()")
f()
print
