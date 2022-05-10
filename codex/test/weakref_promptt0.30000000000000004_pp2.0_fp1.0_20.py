import weakref
# Test weakref.ref()
import weakref
class Foo(object):
    pass
f = Foo()
r = weakref.ref(f)
