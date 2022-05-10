import weakref
# Test weakref.ref(obj)
class Foo(object):
    pass

foo = Foo()

# Test weakref.ref(obj, callback)
def callback(ref):
    print("callback called with %r" % (ref,))

ref = weakref.ref(foo, callback)

# Test weakref.getweakrefcount(obj)
print("count:", weakref.getweakrefcount(foo))

# Test weakref.getweakrefs(obj)
refs = weakref.getweakrefs(foo)
print("refs:", refs)

# Test weakref.proxy(obj, callback)
proxy = weakref.proxy(foo, callback)

# Test weakref.finalize(obj, callback, *args, **kwds)
def finalize_callback(arg):
    print("finalize_callback called with %r" % (arg,))

finalizer = weakref.finalize(foo, finalize_callback, "hello")

# Test weakref.WeakKeyDictionary
class Foo(object):
    pass

foo1 = Foo()

