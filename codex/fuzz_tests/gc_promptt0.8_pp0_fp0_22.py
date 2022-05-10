import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a file object.
import gc, weakref
f = open(__file__)
r = weakref.ref(f)
f.close()
gc.collect()
if r() is not None:
    print('collect() did not clean up the file object')
gc.set_debug(0)
# Test weakref on static methods.
import gc, weakref
class Bar(object):
    def foo(self):
        pass
    def foo2(self):
        pass
    foo = staticmethod(foo)
    foo2 = classmethod(foo2)

b = Bar()
for sm in (Bar.foo, Bar.foo2, b.foo, b.foo2):
    print('%s: %s' % (sm, weakref.ref(sm)))
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a unicode string containing NULL bytes.
import gc, weakref
s = 'hello\x00world'
u = s.decode('latin-1')
r = weakref.ref
