import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() as we don't do it as we used to do it when
# needed in Python 2.X, so we want to make sure not to trigger
# errors by accidently calling it too often.

# Null pointers evaluated lazily

lazynullptrs = [weakref.proxy(None), ]
print(lazynullptrs[0]) # should not crash

class X:
    pass

class Y:
    pass

class A:
    pass

class B(A):
    def __init__(self):
        weakref.proxy(Y())
        self.x = X()
        B.z = X()

B.z = X()
a = weakref.proxy(A())
b = weakref.proxy(B())
gc.collect()

# Test that gc collects self-referential objects.

class C:
    def __init__(self):
        self.cs = [self]

c = C()

# The last thing we do is to make sure that the number of objects left
# after a full collection is still correct.  The correct
