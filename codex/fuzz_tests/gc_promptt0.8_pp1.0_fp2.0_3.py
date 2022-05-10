import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
print "Checking collection..."
import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
class A:
    pass
a = A()
w1 = weakref.ref(a)
w2 = weakref.ref(a)
a = None
# The following line is expected to fail
print gc.collect()
print gc.collect()
print gc.collect()
# Test weakref.WeakSet
print "Testing WeakSet"
import weakref, gc
foo = None
bar = SomeClass()
bar.chicken = 'joe'
class SomeClass:
    def __del__(self):
        print 'dead'
sss = SomeClass()
sss.foo = 'bar'
bar.refs = []
bar.refs.append(weakref.ref(foo))
bar.refs.append(weakref.ref(sss))
bar.refs.append(weakref.ref(bar))
print bar.chicken
del bar
print bar.chicken
print bar.refs[
