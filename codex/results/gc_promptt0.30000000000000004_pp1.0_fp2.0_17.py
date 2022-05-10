import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to a class instance
# Note that the class instance is not collectable until the weakref is deleted

class A:
    pass

a = A()
w = weakref.ref(a)

print 'before:', gc.collect()
del a
print 'after:', gc.collect()

del w
print 'finally:', gc.collect()
