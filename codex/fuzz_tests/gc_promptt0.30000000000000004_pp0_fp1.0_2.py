import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

class B(A):
    pass

class C(A):
    pass

def f():
    a = A()
    b = B()
    c = C()
    a.b = b
    a.c = c
    b.a = a
    b.c = c
    c.a = a
    c.b = b
    w = weakref.ref(a)
    del a, b, c
    return w

w = f()
gc.collect()
print w() is None

# Test gc.collect() with a weakref to an instance method

class D:
    def f(self):
        pass

d = D()
w = weakref.ref(d.f)
del d
gc.collect()
print w() is None

# Test gc.collect() with a weakref to a class method

class E:
    def f(cls):
        pass
    f = classmethod(f)

e = E()
w = weakref
