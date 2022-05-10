import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(object):
    pass

class F(E):
    pass

class G(E):
    pass

class H(F, G):
    pass

for cls in [A, B, C, D, E, F, G, H]:
    print cls, len(gc.get_referrers(cls))

# When tp_clear is called on a type, the type's tp_dealloc slot will be
# called.  This can cause problems if the type has a weakref to itself.
# This can happen with extension types, but we have to cheat a bit to
# cause it to happen with a pure Python type.

class X(object):
    def __init__(self):
        self.wr = weakref.ref(self)

x = X()

X_ID = id(X)

# create a reference cycle
x.y =
