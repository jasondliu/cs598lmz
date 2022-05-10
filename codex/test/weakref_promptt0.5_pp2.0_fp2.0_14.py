import weakref
# Test weakref.ref(x)
# Test weakref.proxy(x)
# Test weakref.getweakrefcount(x)
# Test weakref.getweakrefs(x)
# Test weakref.WeakKeyDictionary()
# Test weakref.WeakValueDictionary()
# Test weakref.WeakSet()
# Test weakref.WeakMethod()
# Test weakref.finalize()
# Test weakref.ReferenceType()
# Test weakref.ProxyType()
# Test weakref.CallableProxyType()
# Test weakref.ProxyTypes
# Test weakref.getweakrefcount()
# Test weakref.getweakrefs()
# Test weakref.ReferenceError

class TestFailing:

    def test_basic(self):
        class Foo:
            pass
        a = Foo()
        r = weakref.ref(a)
        r()

    def test_basic_exception(self):
        class Foo:
            pass
        a = Foo()
        r = weakref.ref(a)
        with self.assertRaises(ReferenceError):
            r()

   
