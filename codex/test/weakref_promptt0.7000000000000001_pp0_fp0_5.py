import weakref
# Test weakref.ref

# TODO: Needs tests for the hash and compare

from test.test_support import run_unittest


class Foo(object):
    pass

class FooSubclass(Foo):
    pass

class FooSubclass2(Foo):
    pass

class FooSubclass3(Foo):
    pass

class FooSubclass4(Foo):
    pass


class MyWeakRef(weakref.ref):

    def __new__(cls, ob):
        return weakref.ref.__new__(cls, ob, cls.callback)

    def callback(wr, selfref):
        selfref._called = True


class MyWeakRef2(weakref.ref):

    def __new__(cls, ob):
        return weakref.ref.__new__(cls, ob, cls.callback)

    def callback(wr, selfref):
        selfref._called = True


class MyWeakRef3(weakref.ref):

    def __new__(cls, ob):
        return weakref.ref.__
