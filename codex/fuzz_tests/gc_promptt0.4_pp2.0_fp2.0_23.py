import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    def __del__(self):
        print 'deleting A'

class B(A):
    pass

class C(A):
    def __del__(self):
        print 'deleting C'
        A.__del__(self)

class D(C, B):
    pass

gc.collect()

a = A()
b = B()
c = C()
d = D()

gc.collect()

print 'deleting a'
del a
gc.collect()

print 'deleting b'
del b
gc.collect()

print 'deleting c'
del c
gc.collect()

print 'deleting d'
del d
gc.collect()
