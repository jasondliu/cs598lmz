import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    a = [1]
    b = [a,a]
    a.append(b)
    ida = id(a)
    del a,b
    return ida

ida = f()
gc.collect()
print(gc.collect())
print(gc.garbage)
print([o for o in gc.get_objects() if id(o) == ida])
print(gc.garbage)
# Test gc.garbage
def f():
    a = [1]
    b = [a,a]
    a.append(b)
    ida = id(a)
    del a,b
    return ida

ida = f()
print(gc.collect())
print(gc.garbage)
print([o for o in gc.get_objects() if id(o) == ida])
print(gc.garbage)
# Test gc.get_objects()
def f():
    a = [1]
    b = [a,a]
    a.append(b)
    
