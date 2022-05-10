import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def foo():
    pass

class MyWeakCallableMethod(weakref.WeakMethod):

    def __call__(self, *args, **kw):
        return super(MyWeakCallableMethod, self).__call__(*args, **kw)

try:
    x = Foo()
    x.foo = foo
    f = x.foo
    x = None
    f()
    print("oops, I should have been gc'ed")
except ReferenceError:
    pass
f = x = None

# Test that weak references to instance methods can be called
class Foo(object):
    def __init__(self):
        pass

    def bar(self):
        pass

foo = Foo()
f = weakref.WeakCallableMethod(foo.bar)

assert f() == None

foo = f = None
gc.collect()

# Test that an object with a __weakref__ callback can have a
# WeakCallableMethod for a method.
class Foo(object):
    def __init__(self
