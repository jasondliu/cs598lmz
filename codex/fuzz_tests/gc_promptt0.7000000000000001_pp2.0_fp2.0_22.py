import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weak reference to an object in the
# unreachable cycle.

class A:
    pass

class B:
    pass

a = A()
b = B()
a.b = b
b.a = a

a_wr = weakref.ref(a)
b_wr = weakref.ref(b)

del a, b

gc.collect()

assert a_wr() is None, "cycle was not collected"
assert b_wr() is None, "cycle was not collected"

# test gc.collect() with a weak reference to an object in the
# unreachable cycle, and an object with a __del__ method.

class C:
    def __del__(self):
        pass

c = C()
c.a = a
a.c = c

c_wr = weakref.ref(c)

del a, c

gc.collect()

assert a_wr() is None, "cycle was not collected"
assert c_wr() is None, "cycle was not collected"
