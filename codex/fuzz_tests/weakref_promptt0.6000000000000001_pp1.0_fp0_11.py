import weakref
# Test weakref.ref()
import collections
a = []
ref = weakref.ref(a)
assert ref() is a
# Test weakref.proxy()
a = []
p = weakref.proxy(a)
assert repr(p) == repr(a)
# Test del
class Foo(object):
    pass
foo = Foo()
foo_ref = weakref.ref(foo)
assert foo_ref() is foo
del foo
assert foo_ref() is None
# Test weakref.finalize()
class Foo(object):
    pass
foo = Foo()
finalizer = weakref.finalize(foo, lambda: None)
assert finalizer.alive
del foo
assert not finalizer.alive
# Test weakref.WeakKeyDictionary
a = B = None
def f():
    global a, B
    a = []
    B = weakref.WeakKeyDictionary()
    B[a] = 42
    a = None
f()
# Test weakref.WeakValueDictionary
a = B = None
def f():
    global a, B
    a = []
   
