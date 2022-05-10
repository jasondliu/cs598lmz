import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs
class Foo:
    pass
obj = Foo()
obj.wr = weakref.ref(obj)
print "foo = ", obj, "weak = ", obj.wr, "id = ", id(obj)
print "obj.wr() = ", obj.wr()
print "obj.__dict__ = ", obj.__dict__
print "obj.__dict__['wr']() = ", obj.__dict__['wr']()
Foo._del = obj._del
del obj
gc.collect()
print "End of test"

# Test gc.get_referrers with weakrefs
obj = Foo()
obj.wr = weakref.ref(obj)
print "obj.wr() = ", obj.wr()
print "obj.__dict__ = ", obj.__dict__
print "obj.__dict__['wr']() = ", obj.__dict__['wr']()
del obj
gc.collect()
print "End of test"

# Test gc.get_referrers with gc.DEBUG_SAVEALL
class A:
    pass

