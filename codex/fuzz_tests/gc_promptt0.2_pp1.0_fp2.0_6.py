import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test weakref.ref()
def callback(arg):
    print 'callback', arg

class A:
    pass

a = A()
w = weakref.ref(a, callback)
print w
print w()
del a
gc.collect()
print w
print w()

# Test weakref.proxy()
a = A()
w = weakref.proxy(a, callback)
print w
print w.__class__
print w.__dict__
print w.__doc__
print w.__module__
print w.__weakref__
print w.__str__()
print w.__repr__()
print w.__nonzero__()
print w.__hash__()
print w.__cmp__(w)
print w.__eq__(w)
print w.__ne__(w)
print w.__lt__(w)
print w.__le__(w)
print w.__gt__(w)
print w.__ge__(w)
print w.__getattr__('__
