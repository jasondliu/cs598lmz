import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs that are still alive
print("\nTesting gc.collect()...")

class A(object):
    pass

class B(object):
    pass

a = A()
b = B()

a_wr = weakref.ref(a)
b_wr = weakref.ref(b)
a_wr2 = weakref.ref(a)

print("Before garbage collection:")
print("    ", a)
print("    ", b)
print("    ", a_wr)
print("    ", b_wr)
print("    ", a_wr2)

gc.collect()

print("After garbage collection:")
print("    ", a)
print("    ", b)
print("    ", a_wr)
print("    ", b_wr)
print("    ", a_wr2)

del a, b, a_wr, b_wr, a_wr2

gc.collect()


# Test gc.collect with weakrefs that are no longer alive
print("\nTesting gc.collect()...")


