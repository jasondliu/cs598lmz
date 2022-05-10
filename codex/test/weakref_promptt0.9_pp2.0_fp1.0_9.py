import weakref
# Test weakref.ref
# Lists of object refs
import weakref
import gc

a = []
class Foo(object):
    pass
foo = Foo()
