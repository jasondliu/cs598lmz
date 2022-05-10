import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B:
    pass

class C:
    pass

a = A()
b = B()
c = C()

a.b = b
b.a = a

a.c = c
c.a = a

del a, b, c

gc.collect()

print gc.collect()
print gc.garbage

# Test gc.garbage

class A:
    pass

class B:
    pass

class C:
    pass

a = A()
b = B()
c = C()

a.b = b
b.a = a

a.c = c
c.a = a

del a, b, c

gc.collect()

print gc.collect()
print gc.garbage

# Test gc.get_debug()

print gc.get_debug()

# Test gc.get_threshold()

print gc.get_threshold()

# Test gc.set_debug()
