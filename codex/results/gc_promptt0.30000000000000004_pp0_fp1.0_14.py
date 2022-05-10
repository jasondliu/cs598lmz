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

x = D()
x.a = A()
x.b = B()
x.c = C()

l = [A(), B(), C(), D()]
l.append(l)

w = weakref.ref(A())

del x, l
gc.collect()

# Test gc.get_referrers()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

x = D()
x.a = A()
x.b = B()
x.c = C()

l = [A(), B(), C(), D()]
l.append(l)

w = weakref.ref(A())

del x, l
gc.collect()

# Test gc.get_referents()

class A:
    pass
