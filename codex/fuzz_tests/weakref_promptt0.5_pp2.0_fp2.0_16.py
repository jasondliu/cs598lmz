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
    if r() is None:
        print "ok"
    else:
        print "not ok"
f()
# Test weakref.WeakKeyDictionary
class Foo(object):
    pass
def f():
    d = weakref.WeakKeyDictionary()
    foo = Foo()
    d[foo] = 1
    foo = None
    gc.collect()
    if d:
        print "not ok"
    else:
        print "ok"
f()
# Test weakref.WeakValueDictionary
class Foo(object):
    pass
def f():
    d = weakref.WeakValueDictionary()
    foo = Foo()
    d["foo"] = foo
    foo = None
    gc.collect()
    if d:
        print "not ok"
    else:
        print "ok"
f()
