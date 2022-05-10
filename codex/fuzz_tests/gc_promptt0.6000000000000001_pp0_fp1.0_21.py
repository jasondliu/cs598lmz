import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without a cyclic trashcan
class A:
    pass
a = A()
def bye():
    print 'bye!'
w = weakref.ref(a, bye)
print 'count:', sys.getcount()
del a
gc.collect()
print 'count:', sys.getcount()

class B:
    pass
b = B()
w = weakref.ref(b)
print 'count:', sys.getcount()
del b
gc.collect()
print 'count:', sys.getcount()

# Test gc.collect() with a cyclic trashcan
class C:
    pass
c = C()
w = weakref.ref(c)
c.cycle = c
print 'count:', sys.getcount()
del c
gc.collect()
print 'count:', sys.getcount()

# Test gc.collect() with a cyclic trashcan that has a __del__ method
class D:
    def __del__(self):
        pass
d = D()
w = weakref.ref(d)
d.cycle =
