import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()


class A:
    pass


class B:
    pass


class C:
    pass


class D:
    pass


def force_gc():
    # Create a cycle with one uncollectable object
    a = A()
    b = B()
    c = C()
    d = D()
    a.x = b
    b.y = c
    c.z = a
    a = b = c = None

    # Now create a cycle with *two* uncollectable objects
    a = A()
    b = B()
    a.x = b
    b.x = a
    del a, b  # Get rid of the last refs to a and b

    # And one more with *three* uncollectable objects
    a = A()
    b = B()
    c = C()
    a.x = b
    b.x = c
    c.x = a
    del a, b, c  # Get rid of the last refs to a and b


N = 50
for i in range(N):
   
