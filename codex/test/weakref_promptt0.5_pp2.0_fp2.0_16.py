import weakref
# Test weakref.ref
import gc
class Foo(object):
    pass
def f():
    foo = Foo()
    r = weakref.ref(foo)
    foo = None
    gc.collect()
