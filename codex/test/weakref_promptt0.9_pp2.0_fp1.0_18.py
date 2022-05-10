import weakref
# Test weakref.ref
import weakref
class Foo(object):
    pass
a = Foo()
r = weakref.ref(a)
