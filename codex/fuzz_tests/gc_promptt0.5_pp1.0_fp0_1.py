import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref.
class A:
    pass

a = A()
wr = weakref.ref(a)
gc.collect()
print wr(), wr() is a
del a
gc.collect()
print wr()

# Test gc.collect() with uncollectable objects.
class B:
    pass

b = B()
b.b = b
gc.collect()
print gc.collect()

# Test gc.collect() with a frame.
def f():
    l = [1, 2, 3]
    gc.collect()

f()
gc.collect()

# Test gc.collect() with an instance method.
class C(object):
    def m(self):
        pass

c = C()
gc.collect()

# Test gc.collect() with a class.
class D:
    pass

d = D()
gc.collect()

# Test gc.collect() with a class method.
class E(object):
    @classmethod
    def cm(cls):
        pass

e =
