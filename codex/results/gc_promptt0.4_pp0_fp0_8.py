import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A(object):
    pass

class B(object):
    pass

class C(object):
    pass

class D(object):
    pass

a = A()
b = B()
c = C()
d = D()

# Create a cycle with a weakref
wr = weakref.ref(a)
a.cycle = wr
del wr

# Create a cycle with a weakproxy
wp = weakref.proxy(b)
b.cycle = wp
del wp

# Create a cycle with a weaklist
wl = weakref.WeakList()
wl.append(c)
c.cycle = wl
del wl

# Create a cycle with a weakdict
wd = weakref.WeakKeyDictionary()
wd[d] = None
d.cycle = wd
del wd

# Create a cycle with a weakvalue dict
wd = weakref.WeakValueDictionary()
wd[1] = d
d.cycle = wd
del wd

# Check that the objects are collectable
gc.
