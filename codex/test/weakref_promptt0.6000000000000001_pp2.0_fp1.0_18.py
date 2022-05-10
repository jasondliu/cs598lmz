import weakref
# Test weakref.ref() on custom objects.
class Foo(object):
    pass

f = Foo()
r = weakref.ref(f)
# Test weakref.ref() on built-in objects.
import sys
r = weakref.ref(sys)
# Test weakref.ref() on non-objects.
r = weakref.ref(1)
# Test weakref.ref() with a callable.
r = weakref.ref(lambda: None)
# Test weakref.ref() with a callable and a dict.
r = weakref.ref(lambda: None, {})
# Test weakref.ref() with a callable and a dict.
r = weakref.ref(lambda: None, {}, 42)
# Test weakref.proxy() on custom objects.
class Foo(object):
    pass

f = Foo()
p = weakref.proxy(f)
# Test weakref.proxy() on built-in objects.
import sys
p = weakref.proxy(sys)
# Test weakref.proxy() on non-objects.
p = weakref.proxy(1)

