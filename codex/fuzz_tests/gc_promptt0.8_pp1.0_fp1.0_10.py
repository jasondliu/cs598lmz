import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class Foo:
  def __del__(self):
    print 'foo'
r = Foo()
r.a = r
del r
gc.collect()
print "collecting...",
gc.collect()
