import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

def f():
    l = [i for i in range(10)]
    del l
    gc.collect()
    print("collecting")

f()
print("done")

# Test gc.get_referrers()

class A:
    pass

def f():
    a = A()
    l = [a]
    del l
    gc.collect()
    print("collecting")

f()
print("done")

# Test gc.get_referents()

class A:
    pass

def f():
    a = A()
    l = [a]
    del l
    gc.collect()
    print("collecting")

f()
print("done")

# Test gc.get_objects()

class A:
    pass

def f():
    a = A()
    l = [a]
    del l
    gc.collect()
    print("collecting")

f()
print("done")

# Test gc.get_stats()


