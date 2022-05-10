import weakref
# Test weakref.refs on proxy objects.
import weakref
class Foo(object):
    pass
a = Foo()
r = weakref.ref(a)
