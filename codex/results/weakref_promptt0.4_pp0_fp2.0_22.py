import weakref
# Test weakref.ref with a weakref.KeyedRef instance.
import weakref

class Foo(object):
    pass

class KeyedRef(weakref.KeyedRef):
    def __init__(self, ob):
        self.__key = ob
        super(KeyedRef, self).__init__(ob, self.remove)

    def remove(self, wr):
        del self.__key

def test_weakref_ref_KeyedRef():
    f = Foo()
    kr = KeyedRef(f)
    wr = weakref.ref(kr)
    assert wr() is kr
    assert kr.__key is f
    del f
    assert wr() is kr
    assert kr.__key is None
    del kr
    assert wr() is None

# Test weakref.ref with a weakref.WeakMethod instance.
import weakref

class Foo(object):
    def __init__(self, value):
        self.value = value
    def __call__(self):
        return self.value

def test_weakref
