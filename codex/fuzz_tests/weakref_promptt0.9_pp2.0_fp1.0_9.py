import weakref
# Test weakref.ref
# Lists of object refs
import weakref
import gc

a = []
class Foo(object):
    pass
foo = Foo()
def foo_deleted(r):
    print 'foo deleted'
a.append(weakref.ref(foo, foo_deleted))
del foo
gc.collect()
if hasattr(a[0], "__call__"):
    print a[0]()


# Weak-valued dicts
import weakref
import gc

a = {}
class Foo(object):
    pass
foo = Foo()
def foo_deleted(r):
    print 'foo deleted'
a[foo] = weakref.ref(foo, foo_deleted)
foo.key = a
del foo
gc.collect()
print a


# Finalization
class MyRef(object):
    def __init__(self, obj, callback):
        self.obj = weakref.ref(obj)
        self._callback = weakref.ref(callback)
    def __call__(self, ref):
        print 'MyRef called', ref
