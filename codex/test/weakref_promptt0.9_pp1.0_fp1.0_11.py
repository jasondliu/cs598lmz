import weakref
# Test weakref.ref
# weakref.ref(instance, callback=None, kwargs=None)
# Create a weak reference object
# Callback can be a function, a method, or None. 
# If not None, the callback will be invoked when the referent is about to be finalized.
wr = weakref.ref(1)
print(wr())
print(wr)

class Foo(object):
    pass

def foo_check(wr):
    print('will del foo')

foo = Foo()
foo_wr = weakref.ref(foo, foo_check)
del foo

# WeakValueDictionary
# Another built-in class from weakref is WeakValueDictionary. 
# It acts much like a normal dictionary, except that references to objects are weak, 
# and so key-referent mappings are removed if the referent object becomes unreachable 
# due to deletion or garbage collection.
wv_dict = weakref.WeakValueDictionary()
foo1 = Foo()
foo2 = Foo()
foo3 = Foo()
wv_dict['Tom'] = foo1
wv_
