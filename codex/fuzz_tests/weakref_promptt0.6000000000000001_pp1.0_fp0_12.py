import weakref
# Test weakref.ref()
class C:
    pass
r = weakref.ref(C())
# Test weakref.getweakrefcount()
weakref.getweakrefcount(C())
# Test weakref.getweakrefs()
weakref.getweakrefs(C())
# Test weakref.proxy()
r = weakref.proxy(C())
# Test weakref.WeakKeyDictionary()
weakref.WeakKeyDictionary()
# Test weakref.WeakValueDictionary()
weakref.WeakValueDictionary()
# Test weakref.ReferenceType
class C(weakref.ReferenceType):
    pass
# Test weakref.WeakSet()
weakref.WeakSet()
# Test weakref.finalize()
weakref.finalize(C(), lambda: None)
# Test weakref.WeakMethod()
weakref.WeakMethod(C().__repr__, C())
# Test weakref.WeakMethodProxy()
weakref.WeakMethodProxy(C().__repr__, C())
# Test weakref.WeakMethodProxy()
class C:
    def __init__(self, i
