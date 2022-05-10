import weakref
# Test weakref.ref() with a class.
class Foo(object):
    pass

f = Foo()
r = weakref.ref(f)
assert r() is f

f = None
assert r() is None
# Test weakref.ref() with a class instance which has a __del__ method.
class Foo(object):
    def __del__(self):
        pass

f = Foo()
r = weakref.ref(f)
assert r() is f

f = None
assert r() is None
# Test weakref.ref() with a class instance which has a __del__ method
# that raises an exception.
class Foo(object):
    def __del__(self):
        raise Exception

f = Foo()
r = weakref.ref(f)
assert r() is f

f = None
assert r() is None
# Test weakref.ref() with a class instance which has a __del__ method
# that raises an exception.
class Foo(object):
    def __del__(self):
        raise Exception

f = Foo()
r = weakref.ref(
