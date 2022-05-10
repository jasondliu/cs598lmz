import weakref
# Test weakref.ref(SomeType, callback)
class C:
    pass
obj = C()
def callback(w):
    print "deleted", w
r = weakref.ref(obj, callback)
del obj

import gc
gc.collect()

r = sys.getrefcount(B) + 1
print "policy", sys.getrefcount(B)
print "deleted", r
print p
print p.d
print 'before:', gc.get_referents(p)
print 'before gc:', gc.get_referrers(p)
print 'unreachable objects:', gc.garbage
print "calling gc"
gc.collect() 
gc.set_debug(gc.DEBUG_LEAK)
print "done gc"
print 'after:', gc.get_referents(p)
print 'after:', gc.get_referrers(p)
print 'unreachable objects:', gc.garbage

# The following test must run with the PYTHONDEBUG environment variable
# set to "gc".
